"""Optional Pico types resolved from HA's registry before button handling."""

from copy import deepcopy

import pytest
from homeassistant.helpers import device_registry as dr

from custom_components.pico_link import async_setup
from custom_components.pico_link.config import parse_pico_config

# Independent of the production mapping: these are the Lutron type names in
# Home Assistant's "model (type)" device registry format.
MODELS = [
    ("PaddleSwitchPico", "P2B"),
    ("Pico2Button", "2B"),
    ("Pico2ButtonRaiseLower", "2BRL"),
    ("Pico3ButtonRaiseLower", "3BRL"),
    ("Pico4ButtonScene", "4B"),
]


def options(kind):
    if kind == "4B":
        return {
            "buttons": {
                "button_1": [
                    {"action": "scene.turn_on", "target": {"entity_id": "scene.test"}}
                ]
            }
        }
    return {"lights": "light.test"}


@pytest.mark.parametrize("raw_type,kind", MODELS)
@pytest.mark.parametrize("format", ["{}", "PJ2-TEST ({})", " PJ2-TEST ( {} ) "])
async def test_detect_supported_models_without_mutating_input(
    hass, register_pico, raw_type, kind, format
):
    device = register_pico(model=format.format(raw_type))
    raw = {"device_id": device.id, **options(kind)}
    # A shared type must not silently assign the same layout to every remote.
    defaults = {"type": "4B" if kind != "4B" else "2B", "light_low_pct": 25}
    original = deepcopy((raw, defaults))
    detected = parse_pico_config(hass, defaults, raw)
    explicit = parse_pico_config(hass, defaults, {**raw, "type": kind})
    assert detected == explicit
    assert detected.type == kind
    assert (raw, defaults) == original


@pytest.mark.parametrize(
    "model",
    [
        None,
        "",
        "   ",
        "PJ2-3BRL-GXX-X01",  # Model numbers alone do not identify our event profile.
        "UnknownPico",
        "Smart Bridge (SmartBridge)",
        "Fan Speed Controller (CasetaFanSpeedController)",
        "NotPico2Button",
        "PJ2-TEST (Pico2ButtonExtra)",
        "PJ2-TEST (Pico2Button) (Pico3ButtonRaiseLower)",
        "PJ2-TEST (Pico2Button) extra text",
        "Pico2Button / Pico4ButtonScene",
    ],
)
async def test_unrecognized_models_request_explicit_type(hass, register_pico, model):
    device = register_pico(model=model, name="Pico2Button")
    with pytest.raises(ValueError, match="Specify 'type' explicitly"):
        parse_pico_config(hass, {}, {"device_id": device.id, "lights": "light.test"})


async def test_missing_registry_entry_requests_explicit_type(hass):
    with pytest.raises(ValueError, match="no device registry entry"):
        parse_pico_config(hass, {}, {"device_id": "missing", "lights": "light.test"})


async def test_matching_model_from_another_integration_is_not_detected(
    hass, register_pico
):
    device = register_pico(model="Pico2Button", domain="test")
    with pytest.raises(ValueError, match="not registered with the Lutron Caseta"):
        parse_pico_config(hass, {}, {"device_id": device.id, "lights": "light.test"})


async def test_detection_uses_same_name_and_id_precedence(hass, register_pico):
    first = register_pico(model="Pico2Button", serial="one", name="Office Pico")
    second = register_pico(model="Pico3ButtonRaiseLower", serial="two")
    registry = dr.async_get(hass)
    registry.async_update_device(second.id, name_by_user="Office Pico")
    raw = {"name": "Office Pico", "lights": "light.test"}
    assert parse_pico_config(hass, {}, raw).type == "3BRL"
    assert parse_pico_config(hass, {}, {**raw, "device_id": first.id}).type == "2B"
    registry.async_update_device(first.id, name_by_user="Office Pico")
    with pytest.raises(ValueError, match="Multiple devices"):
        parse_pico_config(hass, {}, raw)


@pytest.mark.parametrize("model", [None, "unknown", "Pico3ButtonRaiseLower"])
async def test_explicit_type_wins_even_when_detection_would_fail_or_disagree(
    hass, register_pico, model
):
    device = register_pico(model=model)
    conf = parse_pico_config(
        hass, {}, {"device_id": device.id, "type": " 2b ", "lights": "light.test"}
    )
    assert conf.type == "2B"


@pytest.mark.parametrize("value", [None, "", " ", 2, False, [], {}])
async def test_invalid_explicit_type_does_not_fall_back_to_detection(
    hass, register_pico, value
):
    device = register_pico(model="Pico2Button")
    with pytest.raises(ValueError, match="'type' must be a non-empty string"):
        parse_pico_config(
            hass, {}, {"device_id": device.id, "type": value, "lights": "light.test"}
        )


async def test_unknown_explicit_type_does_not_fall_back_to_detection(
    hass, register_pico
):
    device = register_pico(model="Pico2Button")
    with pytest.raises(ValueError, match="Invalid Pico type"):
        parse_pico_config(
            hass,
            {},
            {"device_id": device.id, "type": "unknown", "lights": "light.test"},
        )


async def test_detected_layout_validates_button_overrides(hass, register_pico):
    device = register_pico(model="Pico2Button")
    with pytest.raises(ValueError, match="not a supported button override for 2B"):
        parse_pico_config(
            hass, {}, {"device_id": device.id, "lights": "light.test", "stop_tap": []}
        )


async def test_unknown_and_duplicate_devices_do_not_disable_valid_remotes(
    registry_pico, register_pico, caplog
):
    known = register_pico(model="Pico2Button", serial="known")
    unknown = register_pico(model="new model", serial="unknown")
    assert await registry_pico.setup(
        [
            {"device_id": unknown.id, "switches": "switch.unknown"},
            {"device_id": "missing", "switches": "switch.missing"},
            {"device_id": known.id, "switches": "switch.detected"},
            {"device_id": known.id, "type": "2B", "switches": "switch.duplicate"},
            {"device_id": "explicit", "type": "P2B", "switches": "switch.explicit"},
        ]
    )
    registry_pico.tap("on", kind="2B", device=known.id)
    registry_pico.tap("on", kind="P2B", device="explicit")
    await registry_pico.drain()
    assert registry_pico.calls == [
        ("switch", "turn_on", {"entity_id": ["switch.detected"]}),
        ("switch", "turn_on", {"entity_id": ["switch.explicit"]}),
    ]
    assert "Specify 'type' explicitly" in caplog.text
    assert "already configured" in caplog.text


@pytest.mark.parametrize("explicit", [False, True])
async def test_hardware_event_mismatch_is_still_rejected(
    registry_pico, register_pico, caplog, explicit
):
    # The explicit case deliberately conflicts with the registry model.
    device = register_pico(model="Pico3ButtonRaiseLower" if explicit else "Pico2Button")
    raw = {"device_id": device.id, "switches": "switch.test"}
    if explicit:
        raw["type"] = "2B"
    assert await registry_pico.setup([raw])
    registry_pico.tap("on", kind="3BRL", device=device.id)
    await registry_pico.drain()
    assert registry_pico.calls == []
    assert "configured as 2B but reported hardware type 3BRL" in caplog.text
    registry_pico.tap("on", kind="2B", device=device.id)
    await registry_pico.drain()
    assert registry_pico.calls == [
        ("switch", "turn_on", {"entity_id": ["switch.test"]})
    ]


async def test_registry_is_not_needed_again_for_button_presses(
    registry_pico, register_pico
):
    device = register_pico(model="Pico2Button")
    assert await registry_pico.setup(
        [{"device_id": device.id, "switches": "switch.test"}]
    )
    # Detection has finished. Losing the registry entry must not make button
    # handling start looking up the model or waiting for discovery again.
    dr.async_get(registry_pico.hass).async_remove_device(device.id)
    registry_pico.tap("on", kind="2B", device=device.id)
    await registry_pico.drain()
    assert registry_pico.calls == [
        ("switch", "turn_on", {"entity_id": ["switch.test"]})
    ]


async def test_later_setup_retries_detection_after_metadata_becomes_available(
    registry_pico, register_pico, caplog
):
    device = register_pico(model=None)
    config = {
        "pico_link": {"devices": [{"device_id": device.id, "switches": "switch.test"}]}
    }
    assert await async_setup(registry_pico.hass, config)
    registry_pico.tap("on", kind="2B", device=device.id)
    await registry_pico.drain()
    assert registry_pico.calls == []
    assert "no valid Pico devices were created" in caplog.text
    dr.async_get(registry_pico.hass).async_update_device(device.id, model="Pico2Button")
    # Run the integration's setup again, as a restart does. No background
    # guessing, delayed commands, or automatic recovery is promised.
    assert await async_setup(registry_pico.hass, config)
    registry_pico.tap("on", kind="2B", device=device.id)
    await registry_pico.drain()
    assert registry_pico.calls == [
        ("switch", "turn_on", {"entity_id": ["switch.test"]})
    ]


async def test_new_setup_uses_updated_model_without_reinterpreting_active_controller(
    registry_pico, register_pico
):
    device = register_pico(model="Pico2Button")
    raw = {"device_id": device.id, "switches": "switch.test"}
    assert await registry_pico.setup([raw])
    dr.async_get(registry_pico.hass).async_update_device(
        device.id, model="Pico3ButtonRaiseLower"
    )
    registry_pico.tap("on", kind="2B", device=device.id)
    await registry_pico.drain()
    assert len(registry_pico.calls) == 1
    await registry_pico.stop()
    assert await async_setup(registry_pico.hass, {"pico_link": {"devices": [raw]}})
    registry_pico.tap("off", kind="3BRL", device=device.id)
    await registry_pico.drain()
    assert registry_pico.calls[-1] == (
        "switch",
        "turn_off",
        {"entity_id": ["switch.test"]},
    )
    assert len(registry_pico.calls) == 2
