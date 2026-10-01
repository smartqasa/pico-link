"""Exercise the real picker entity, target expansion and registry identity."""

from copy import deepcopy

import pytest
from homeassistant.components.light import ColorMode, LightEntityFeature
from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers import entity_registry as er
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import (
    MockConfigEntry,
    MockModule,
    mock_integration,
)

from custom_components.pico_link.config import parse_pico_config
from custom_components.pico_link.const import DOMAIN
from custom_components.pico_link.panel import panel_state
from custom_components.pico_link.placeholder import (
    NAME,
    UNIQUE_ID,
    placeholder_entity_id,
)


async def test_real_light_capabilities_and_direct_use(hass, enable_custom_integrations):
    mock_integration(hass, MockModule("lutron_caseta"))
    assert await async_setup_component(hass, DOMAIN, {})
    await hass.async_block_till_done()
    entity_id = placeholder_entity_id(hass)
    assert entity_id == "light.pico_link_placeholder"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.attributes["friendly_name"] == NAME
    assert {ColorMode.RGB, ColorMode.COLOR_TEMP}.issubset(
        state.attributes["supported_color_modes"]
    )
    assert state.attributes["min_color_temp_kelvin"] == 1000
    assert state.attributes["max_color_temp_kelvin"] == 40000
    for feature in (
        LightEntityFeature.EFFECT,
        LightEntityFeature.FLASH,
        LightEntityFeature.TRANSITION,
    ):
        assert state.attributes["supported_features"] & feature
    for service, data in [
        ("turn_on", {"brightness_pct": 80, "color_temp_kelvin": 2800}),
        ("turn_on", {"rgb_color": [0, 0, 255]}),
        ("turn_off", {}),
    ]:
        with pytest.raises(ServiceValidationError, match="triggering Pico"):
            await hass.services.async_call(
                "light", service, {"entity_id": entity_id, **data}, blocking=True
            )
    assert hass.states.get(entity_id).state == "off"


async def test_registry_reuses_existing_identity_and_respects_collision(
    hass, registry_pico
):
    registry = er.async_get(hass)
    unrelated = registry.async_get_or_create(
        "light", "other", "real-light", suggested_object_id=UNIQUE_ID
    )
    assert await registry_pico.setup([])
    await registry_pico.drain()
    entity_id = placeholder_entity_id(hass)
    assert entity_id == "light.pico_link_placeholder_2"
    assert registry.async_get(unrelated.entity_id).platform == "other"
    registry.async_update_entity(
        entity_id, new_entity_id="light.my_pico_placeholder", name="My Pico lights"
    )
    await registry_pico.drain()
    assert placeholder_entity_id(hass) == "light.my_pico_placeholder"
    info = panel_state(hass)["light_placeholder"]
    assert info == {"entity_id": "light.my_pico_placeholder", "name": "My Pico lights"}
    conf = parse_pico_config(
        hass,
        {},
        {
            "device_id": "pico",
            "type": "3BRL",
            "lights": ["light.actual"],
            "stop_tap": [
                {
                    "action": "light.turn_on",
                    "target": {"entity_id": [unrelated.entity_id, info["entity_id"]]},
                }
            ],
        },
    )
    assert conf.overrides["stop_tap"][0]["target"]["entity_id"] == [
        unrelated.entity_id,
        "light.actual",
    ]


@pytest.mark.parametrize("gesture", ["tap", "hold", "double_tap"])
@pytest.mark.parametrize("shared", [False, True])
async def test_per_pico_expansion_preserves_nested_actions_and_explicit_targets(
    hass, registry_pico, gesture, shared
):
    assert await registry_pico.setup([])
    await registry_pico.drain()
    placeholder = placeholder_entity_id(hass)
    key = f"stop_{gesture}" if shared else f"on_{gesture}"
    action = {
        "action": "light.turn_on",
        "target": {"entity_id": [placeholder, "light.fixed"]},
        "data": {"brightness_pct": 80, "color_temp_kelvin": 2800},
        "continue_on_error": True,
    }
    sequence = [
        {
            "choose": [
                {
                    "conditions": "{{ true }}",
                    "sequence": [{"repeat": {"count": 2, "sequence": [action]}}],
                }
            ],
            "default": [
                {"action": "light.turn_off", "target": {"entity_id": "light.fixed"}}
            ],
        }
    ]
    defaults = {key: sequence} if shared else {}
    original = deepcopy(sequence)
    for assigned in [["light.kitchen"], ["light.bedroom", "light.bedside"]]:
        conf = parse_pico_config(
            hass,
            defaults,
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": assigned,
                key: "default" if shared else sequence,
            },
        )
        resolved = conf.overrides[key][0]
        assert resolved["choose"][0]["sequence"][0]["repeat"]["sequence"][0] == {
            **action,
            "target": {"entity_id": [*assigned, "light.fixed"]},
        }
        assert resolved["default"] == original[0]["default"]
    assert sequence == original
    if shared:
        assert defaults[key] == original


async def test_physical_event_runs_assigned_light_action_and_fixed_step(
    hass, registry_pico, register_pico
):
    remote = register_pico(model="Test (Pico3ButtonRaiseLower)")
    assert await registry_pico.setup([])
    await registry_pico.drain()
    placeholder = placeholder_entity_id(hass)
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id=DOMAIN,
        data={
            "defaults": {
                "stop_tap": [
                    {
                        "action": "light.turn_on",
                        "target": {"entity_id": placeholder},
                        "data": {"brightness_pct": 80, "color_temp_kelvin": 2800},
                    },
                    {
                        "action": "light.turn_off",
                        "target": {"entity_id": "light.fixed"},
                    },
                ]
            },
            "devices": [
                {
                    "device_id": remote.id,
                    "lights": ["light.desk"],
                    "stop_tap": "default",
                }
            ],
        },
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await registry_pico.drain()
    for _ in range(2):
        registry_pico.tap("stop", device=remote.id)
        await registry_pico.drain()
        assert registry_pico.calls[-2][2] == {
            "entity_id": ["light.desk"],
            "brightness_pct": 80,
            "color_temp_kelvin": 2800,
        }
        assert registry_pico.calls[-1][2] == {"entity_id": "light.fixed"}
        assert await hass.config_entries.async_reload(entry.entry_id)
        await registry_pico.drain()
        assert placeholder_entity_id(hass) == placeholder
        assert hass.states.get(placeholder) is not None
    records = er.async_get(hass).entities
    assert (
        len(
            [
                e
                for e in records.values()
                if e.platform == DOMAIN and e.unique_id == UNIQUE_ID
            ]
        )
        == 1
    )


async def test_cannot_assign_placeholder_as_controlled_light(hass, registry_pico):
    assert await registry_pico.setup([])
    with pytest.raises(ValueError, match="Assign real lights"):
        parse_pico_config(
            hass,
            {},
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": [placeholder_entity_id(hass)],
            },
        )


@pytest.mark.parametrize("kind", ["3BRL", "4B"])
@pytest.mark.parametrize("use_legacy", [False, True])
async def test_missing_assignment_is_an_explanatory_error(
    hass, registry_pico, kind, use_legacy
):
    assert await registry_pico.setup([])
    target = "lights" if use_legacy else placeholder_entity_id(hass)
    raw = {"device_id": "pico", "type": kind}
    if kind == "3BRL":
        raw["covers"] = ["cover.shade"]
    raw["on_tap" if kind == "3BRL" else "button_1_tap"] = [
        {"action": "light.turn_on", "target": {"entity_id": [target, "light.fixed"]}}
    ]
    with pytest.raises(ValueError, match="no assigned entities"):
        parse_pico_config(hass, {}, raw)


async def test_existing_registry_record_is_reused_on_startup(hass, registry_pico):
    registry = er.async_get(hass)
    existing = registry.async_get_or_create(
        "light",
        DOMAIN,
        UNIQUE_ID,
        suggested_object_id="renamed_pico_light",
        original_name=NAME,
    )
    original_id = existing.id
    assert await registry_pico.setup([])
    await registry_pico.drain()
    assert placeholder_entity_id(hass) == existing.entity_id
    assert registry.async_get(existing.entity_id).id == original_id
    assert hass.states.get(existing.entity_id) is not None
