"""Public configuration contracts, including device lookup and shared defaults."""

from collections import UserDict
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import patch

import pytest
from homeassistant.helpers import device_registry as dr
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.pico_link.config import lookup_device_id, parse_pico_config


async def test_defaults_and_device_overrides(hass):
    raw = {"device_id": "pico", "type": " 3brl ", "lights": "light.desk"}
    conf = parse_pico_config(hass, {}, raw)
    assert (conf.type, conf.hold_time_ms, conf.step_time_ms) == ("3BRL", 400, 650)
    assert (conf.light_low_pct, conf.light_step_pct, conf.light_on_pct) == (5, 10, 100)
    conf = parse_pico_config(
        hass, {"light_low_pct": 25, "step_time_ms": 900}, {**raw, "step_time_ms": 500}
    )
    assert (conf.light_low_pct, conf.step_time_ms) == (25, 500)


@pytest.mark.parametrize(
    "value,expected",
    [
        (-1, 100),
        (5000, 2000),
        ("750", 750),
        ("bad", 650),
        (None, 650),
        (True, 650),
        (0, 650),
    ],
)
async def test_timing_normalization(hass, value, expected):
    conf = parse_pico_config(
        hass,
        {},
        {
            "device_id": "pico",
            "type": "2B",
            "lights": "light.desk",
            "step_time_ms": value,
        },
    )
    assert conf.step_time_ms == expected


@pytest.mark.parametrize(
    "value,expected", [(True, True), (False, False), ("yes", True), ("false", False)]
)
async def test_cover_inversion_boolean(hass, value, expected):
    conf = parse_pico_config(
        hass,
        {},
        {
            "device_id": "pico",
            "type": "2B",
            "covers": "cover.shade",
            "cover_inverted": value,
        },
    )
    assert conf.cover_inverted is expected


@pytest.mark.parametrize(
    "changes,error",
    [
        ({"type": "unknown"}, "Invalid Pico type"),
        ({"lights": []}, "exactly one"),
        ({"fans": "fan.office"}, "multiple entity domains"),
        ({"lights": "fan.office"}, "domain"),
        ({"lights": "not_an_entity"}, "invalid entity ID"),
        ({"lights": [None]}, "must be a string"),
        ({"device_id": " "}, "non-empty string"),
        ({"cover_inverted": "maybe"}, "Boolean"),
        ({"middle_button": {"action": "light.turn_on"}}, "list of actions"),
        ({"middle_button": [{"action": "invalid"}]}, "domain.service"),
        ({"middle_button": [{"action": "light.turn_on", "data": []}]}, "mapping"),
        ({"middle_button": [{"action": "light.turn_on", "target": []}]}, "mapping"),
        ({"type": "2B", "middle_button": [{"action": "light.turn_on"}]}, "3BRL"),
        ({"buttons": {"button_1": [{"action": "scene.turn_on"}]}}, "only valid for 4B"),
    ],
)
async def test_invalid_device_configuration_is_rejected(hass, changes, error):
    with pytest.raises(ValueError, match=error):
        parse_pico_config(
            hass,
            {},
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": "light.desk",
                **changes,
            },
        )


@pytest.mark.parametrize(
    "buttons", [{}, {"on": [{"action": "scene.turn_on"}]}, {"button_1": []}]
)
async def test_scene_remote_requires_valid_nonempty_button_actions(hass, buttons):
    with pytest.raises(ValueError):
        parse_pico_config(
            hass,
            {},
            {
                "device_id": "pico",
                "type": "4B",
                "buttons": buttons,
            },
        )


async def test_entity_deduplication_and_placeholder_expansion_do_not_mutate_input(hass):
    defaults = {
        "middle_button": [
            {
                "action": "light.turn_on",
                "target": {
                    "entity_id": ["lights", "light.accent"],
                    "area_id": "office",
                },
            }
        ]
    }
    raw = {
        "device_id": "pico",
        "type": "3BRL",
        "lights": ["light.desk", "light.wall", "light.desk"],
        "middle_button": "default",
    }
    original = deepcopy((defaults, raw))
    conf = parse_pico_config(hass, defaults, raw)
    assert conf.lights == ["light.desk", "light.wall"]
    assert conf.middle_button[0]["target"] == {
        "entity_id": ["light.desk", "light.wall", "light.accent"],
        "area_id": "office",
    }
    assert (defaults, raw) == original


@pytest.mark.parametrize(
    "setting,expected",
    [
        (None, []),
        ([], []),
        ("default", [{"action": "scene.turn_on"}]),
        ([{"action": "script.turn_on"}], [{"action": "script.turn_on"}]),
    ],
)
async def test_middle_button_defaults_require_explicit_opt_in(hass, setting, expected):
    conf = parse_pico_config(
        hass,
        {"middle_button": [{"action": "scene.turn_on"}]},
        {
            "device_id": "pico",
            "type": "3BRL",
            "lights": "light.desk",
            "middle_button": setting,
        },
    )
    assert conf.middle_button == expected


async def test_device_names_prefer_user_name_and_reject_ambiguous_names(hass, caplog):
    entry = MockConfigEntry(domain="lutron_caseta")
    entry.add_to_hass(hass)
    registry = dr.async_get(hass)
    first = registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={("lutron_caseta", "one")},
        name="Office Pico",
    )
    second = registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={("lutron_caseta", "two")},
        name="Other Pico",
    )
    registry.async_update_device(second.id, name_by_user="Office Pico")
    raw = {"name": "Office Pico", "type": "2B", "lights": "light.desk"}
    assert parse_pico_config(hass, {}, raw).device_id == second.id
    # An explicit ID wins even when a name was also provided.
    assert (
        parse_pico_config(hass, {}, {**raw, "device_id": first.id}).device_id
        == first.id
    )
    registry.async_update_device(first.id, name_by_user="Office Pico")
    with pytest.raises(ValueError, match="Multiple devices"):
        parse_pico_config(hass, {}, raw)
    with pytest.raises(ValueError, match="No device was found"):
        parse_pico_config(hass, {}, {**raw, "name": "Missing Pico"})
    assert "uses `device_registry.devices` as a mapping" not in caplog.text


@pytest.mark.parametrize("container", [dict, UserDict, tuple, iter])
async def test_device_lookup_supports_old_mappings_and_entry_iterables(hass, container):
    """Keep old HA name precedence and ambiguity rules on the new collection API."""
    first = SimpleNamespace(id="one", name="Office Pico", name_by_user=None)
    second = SimpleNamespace(id="two", name="Other Pico", name_by_user="Office Pico")
    third = SimpleNamespace(id="three", name="Duplicate Pico", name_by_user=None)
    fourth = SimpleNamespace(id="four", name="Duplicate Pico", name_by_user=None)

    def registry():
        entries = [first, second, third, fourth]
        devices = (
            container({entry.id: entry for entry in entries})
            if container in (dict, UserDict)
            else container(entries)
        )
        return SimpleNamespace(devices=devices)

    with patch(
        "custom_components.pico_link.config.dr.async_get",
        side_effect=lambda _: registry(),
    ):
        assert lookup_device_id(hass, "Office Pico") == "two"
        assert lookup_device_id(hass, "Other Pico") == "two"
        assert lookup_device_id(hass, "Missing Pico") is None
        with pytest.raises(ValueError, match="Multiple devices"):
            lookup_device_id(hass, "Duplicate Pico")
        first.name_by_user = "Office Pico"
        with pytest.raises(ValueError, match="Multiple devices"):
            lookup_device_id(hass, "Office Pico")


async def test_device_lookup_never_uses_mapping_methods_on_entry_collection(hass):
    """A modern registry may still expose deprecated mapping methods; do not call them."""
    entry = SimpleNamespace(id="one", name="Office Pico", name_by_user=None)

    class EntryCollection:
        def __iter__(self):
            return iter([entry])

        def __getattr__(self, name):
            raise AssertionError(f"Deprecated mapping access: {name}")

    with patch(
        "custom_components.pico_link.config.dr.async_get",
        return_value=SimpleNamespace(devices=EntryCollection()),
    ):
        assert lookup_device_id(hass, "Office Pico") == entry.id
        assert lookup_device_id(hass, "Missing Pico") is None
