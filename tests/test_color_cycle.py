"""Native color cycling through real gesture, service and storage lifecycles."""

import asyncio
from copy import deepcopy
from unittest.mock import patch

import pytest
from homeassistant.const import EVENT_HOMEASSISTANT_FINAL_WRITE
from homeassistant.exceptions import HomeAssistantError

from custom_components.pico_link.color_cycle import (
    DEFAULT_PALETTE,
    PALETTE_GESTURES,
    STORAGE_KEY,
    ColorCycleStore,
    get_cycle_store,
    migrate_palette_document,
    normalize_palette,
)
from custom_components.pico_link.config import parse_pico_config
from custom_components.pico_link.controller import PicoController
from custom_components.pico_link.ui_config import validate_document

RED = {"rgb_color": [255, 0, 0]}
BLUE = {"rgb_color": [0, 0, 255]}
WHITE = {"color_temp_kelvin": 2800}
PALETTE = [RED, WHITE, BLUE]


def config(**values):
    return {
        "device_id": "pico",
        "type": "3BRL",
        "lights": ["light.a", "light.b"],
        "stop_tap": "color_cycle",
        **values,
    }


@pytest.mark.parametrize("gesture", ["tap", "hold", "double_tap"])
async def test_cycle_gestures_once_and_wrap_without_reading_light_state(pico, gesture):
    raw = (
        config(stop_tap=[], **{f"stop_{gesture}": "color_cycle"})
        if gesture != "tap"
        else config()
    )
    assert await pico.setup_ui(
        [raw], {"color_palette": PALETTE, "double_tap_time_ms": 100}
    )
    # These lights can differ, be off or unavailable; they are never our cursor.
    pico.hass.states.async_set("light.a", "off", {"rgb_color": BLUE["rgb_color"]})
    pico.hass.states.async_set("light.b", "unavailable")
    for color in [*PALETTE, RED]:
        pico.fire("stop")
        if gesture == "hold":
            await asyncio.sleep(0.14)
        pico.fire("stop", "release")
        if gesture == "double_tap":
            pico.tap("stop")
        assert await pico.next_call() == (
            "light",
            "turn_on",
            {**color, "entity_id": ["light.a", "light.b"]},
        )
        await pico.drain()
    assert len(pico.calls) == 4


async def test_shared_cycle_is_opt_in_and_custom_palette_is_independent(pico):
    defaults = {"stop_tap": "color_cycle", "color_palette": PALETTE}
    devices = [
        config(device_id="shared", stop_tap="default"),
        config(device_id="custom", color_palette=[BLUE, RED]),
        config(device_id="normal", stop_tap=[]),
    ]
    original = deepcopy((defaults, devices))
    assert await pico.setup_ui(devices, defaults)
    for device, color in [
        ("shared", RED),
        ("custom", BLUE),
        ("shared", WHITE),
        ("custom", RED),
    ]:
        pico.tap("stop", device=device)
        assert (await pico.next_call())[2] == {
            **color,
            "entity_id": ["light.a", "light.b"],
        }
        await pico.drain()
    pico.tap("stop", device="normal")
    await pico.drain()
    assert len(pico.calls) == 4
    assert (defaults, devices) == original


async def test_unconfigured_stop_and_existing_custom_actions_unchanged(pico):
    raw = config()
    del raw["stop_tap"]
    raw["on_tap"] = [
        {
            "action": "light.turn_on",
            "target": {"entity_id": "lights"},
            "data": {"brightness_pct": 42},
        }
    ]
    assert await pico.setup_ui([raw], {"stop_tap": "color_cycle"})
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == []
    assert "color_cycles" not in pico.hass.data["pico_link"]
    pico.tap("on")
    assert (await pico.next_call())[2] == {
        "brightness_pct": 42,
        "entity_id": ["light.a", "light.b"],
    }


@pytest.mark.parametrize(
    "raw",
    [
        config(middle_button="color_cycle", stop_tap=[]),
        config(middle_button="default", stop_tap=[]),
    ],
)
async def test_explicit_stop_tap_wins_over_legacy_cycle(hass, raw):
    conf = parse_pico_config(hass, {"middle_button": "color_cycle"}, raw, from_ui=True)
    assert conf.color_cycle_gestures == set()


@pytest.mark.parametrize("key", ["stop_tap", "middle_button"])
@pytest.mark.parametrize("shared", [False, True])
async def test_cycle_aliases_and_shared_selection(hass, key, shared):
    raw = config()
    del raw["stop_tap"]
    raw[key] = "default" if shared else "color_cycle"
    conf = parse_pico_config(hass, {"stop_tap": "color_cycle"}, raw, from_ui=True)
    assert conf.color_cycle_gestures == {"stop_tap"}
    assert conf.color_palettes["stop_tap"] == DEFAULT_PALETTE


@pytest.mark.parametrize(
    "value",
    [
        [],
        "red",
        None,
        ["red"],
        [{"rgb_color": [256, 0, 0]}],
        [{"rgb_color": [True, 0, 0]}],
        [{"rgb_color": [0, 1]}],
        [{"color_temp_kelvin": 999}],
        [{"color_temp_kelvin": 10001}],
        [{"color_temp_kelvin": 2800.5}],
        [{**RED, "brightness": 30}],
        [RED] * 26,
        [RED] * 33,
    ],
)
async def test_invalid_new_palettes_rejected_in_parser_and_empty_ui_document(
    hass, value
):
    with pytest.raises(ValueError, match="color_palette"):
        parse_pico_config(hass, {"color_palette": value}, config(), from_ui=True)
    with pytest.raises(ValueError, match="color_palette"):
        await validate_document(
            hass, {"defaults": {"color_palette": value}, "devices": []}
        )


@pytest.mark.parametrize("scope", ["shared", "custom"])
async def test_new_palette_limit_is_25(hass, scope):
    for count in (25, 26):
        root = {"defaults": {}, "devices": [config()]}
        target = root["defaults"] if scope == "shared" else root["devices"][0]
        target["color_palette"] = [RED] * count
        if count == 25:
            configs = await validate_document(hass, root)
            assert len(configs[0].color_palettes["stop_tap"]) == count
        else:
            with pytest.raises(ValueError, match="between 1 and 25"):
                await validate_document(hass, root)


@pytest.mark.parametrize("scope", ["shared", "custom"])
@pytest.mark.parametrize(
    "setting",
    [
        {"color_palette": PALETTE},
        {"color_palettes": {"stop_tap": PALETTE}},
        {"stop_tap": "color_cycle"},
        {"stop_hold": "color_cycle"},
        {"stop_double_tap": "color_cycle"},
        {"middle_button": "color_cycle"},
    ],
)
async def test_native_color_settings_require_ui(pico, scope, setting, caplog):
    defaults, device = {}, config(stop_tap=[])
    target = defaults if scope == "shared" else device
    target.update(setting)
    assert await pico.setup([device], defaults)
    assert not pico.hass.data["pico_link"].get("controllers")
    assert (
        "Configure native color cycling and palettes in the Pico Link UI" in caplog.text
    )


async def test_yaml_other_remotes_and_color_actions_remain_supported(pico):
    custom = config(
        device_id="custom",
        stop_tap=[
            {
                "action": "light.turn_on",
                "target": {"entity_id": "lights"},
                "data": {"rgb_color": [128, 0, 255]},
            }
        ],
    )
    assert await pico.setup([config(), custom])
    assert len(pico.hass.data["pico_link"]["controllers"]) == 1
    pico.tap("stop", device="custom")
    assert (await pico.next_call())[2]["rgb_color"] == [128, 0, 255]


@pytest.mark.parametrize("kind", ["2B", "P2B", "2BRL", "4B"])
async def test_other_models_cannot_enable_stop_cycling(hass, kind):
    with pytest.raises(ValueError):
        parse_pico_config(hass, {}, config(type=kind), from_ui=True)


async def test_cycling_requires_assigned_lights_and_stop(hass):
    for raw in [config(lights=[], fans=["fan.a"]), config(on_tap="color_cycle")]:
        with pytest.raises(ValueError, match="requires a 3BRL Stop gesture"):
            parse_pico_config(hass, {}, raw, from_ui=True)


async def test_shutdown_flush_and_fresh_store_resume_by_identity(pico, hass_storage):
    assert await pico.setup_ui([config()], {"color_palette": PALETTE})
    pico.tap("stop")
    await pico.next_call()
    await pico.drain()
    store = get_cycle_store(pico.hass)
    device_id = next(iter(store.positions))
    await pico.stop()
    pico.hass.bus.async_fire(EVENT_HOMEASSISTANT_FINAL_WRITE)
    await pico.drain()
    assert hass_storage[STORAGE_KEY]["data"][device_id]["stop_tap"]["color"] == RED
    restored = ColorCycleStore(pico.hass)
    await restored.async_load()
    await restored.async_cycle(device_id, "stop_tap", ["light.other"], PALETTE)
    assert (await pico.next_call())[2] == {**WHITE, "entity_id": ["light.other"]}


async def test_palette_reload_preserves_color_or_starts_first(pico):
    assert await pico.setup_ui([config()], {"color_palette": PALETTE})
    ctrl = pico.hass.data["pico_link"]["controllers"][0]
    pico.tap("stop")
    await pico.next_call()
    await pico.drain()
    # Same identity, new controller after a UI save; last red moved to index 1.
    await ctrl.async_stop()
    conf = parse_pico_config(
        pico.hass,
        {},
        config(device_id=ctrl.conf.device_id, color_palette=[BLUE, RED, WHITE]),
        from_ui=True,
    )
    reloaded = PicoController(pico.hass, conf)
    await reloaded.async_start()
    try:
        pico.tap("stop")
        assert (await pico.next_call())[2] == {
            **WHITE,
            "entity_id": ["light.a", "light.b"],
        }
        await pico.drain()
    finally:
        await reloaded.async_stop()
    conf.color_palettes["stop_tap"] = [BLUE, RED]
    reloaded = PicoController(pico.hass, conf)
    await reloaded.async_start()
    try:
        pico.tap("stop")
        assert (await pico.next_call())[2] == {
            **BLUE,
            "entity_id": ["light.a", "light.b"],
        }
        await pico.drain()
    finally:
        await reloaded.async_stop()


@pytest.mark.parametrize(
    "mode,expected", [("single", 1), ("queued", 2), ("parallel", 2), ("restart", 2)]
)
async def test_modes_and_runtime_never_update_options(pico, mode, expected):
    gate = asyncio.Event()

    async def slow(_call):
        await gate.wait()

    pico.register("light", "turn_on", slow)
    assert await pico.setup_ui([config(mode=mode, max=2)], {"color_palette": PALETTE})
    with patch.object(pico.hass.config_entries, "async_update_entry") as update:
        pico.tap("stop")
        await pico.next_call()
        pico.tap("stop")
        await asyncio.sleep(0.03)
        gate.set()
        await pico.drain()
        assert len(pico.calls) == expected
        update.assert_not_called()
    # Serial execution gives queued/parallel requests successive colors.
    if mode in {"queued", "parallel"}:
        assert pico.calls[1][2]["color_temp_kelvin"] == 2800


async def test_slow_pico_does_not_block_another_with_overlapping_targets(pico):
    gate = asyncio.Event()

    async def slow(call):
        if "light.slow" in call.data["entity_id"]:
            await gate.wait()

    pico.register("light", "turn_on", slow)
    assert await pico.setup_ui(
        [
            config(device_id="slow", lights=["light.a", "light.slow"]),
            config(device_id="fast", lights=["light.a"]),
        ],
        {"color_palette": PALETTE},
    )
    pico.tap("stop", device="slow")
    await pico.next_call()
    pico.tap("stop", device="fast")
    assert (await pico.next_call())[2] == {**RED, "entity_id": ["light.a"]}
    await asyncio.sleep(0.02)
    pico.tap("stop", device="fast")
    assert (await pico.next_call())[2] == {**WHITE, "entity_id": ["light.a"]}
    gate.set()
    await pico.drain()


async def test_service_failure_retries_same_color_and_shutdown_cancels(pico):
    async def fail(_call):
        raise HomeAssistantError("Light unavailable")

    pico.register("light", "turn_on", fail)
    assert await pico.setup_ui([config(mode="queued")], {"color_palette": PALETTE})
    pico.tap("stop")
    await pico.next_call()
    await pico.drain()
    assert get_cycle_store(pico.hass).positions == {}
    gate = asyncio.Event()

    async def slow(_call):
        await gate.wait()

    pico.register("light", "turn_on", slow)
    pico.tap("stop")
    assert (await pico.next_call())[2] == {**RED, "entity_id": ["light.a", "light.b"]}
    pico.tap("stop")
    await asyncio.sleep(0.02)
    ctrl = pico.hass.data["pico_link"]["controllers"][0]
    await ctrl.async_stop()
    gate.set()
    await pico.drain()
    assert len(pico.calls) == 2
    assert get_cycle_store(pico.hass).positions == {}


async def test_corrupt_saved_positions_are_ignored(hass, hass_storage):
    hass_storage[STORAGE_KEY] = {
        "version": 1,
        "data": {
            "bad": {"index": -1, "color": RED},
            "unknown": "bad",
            "invalid": {"index": 0, "color": {"rgb_color": []}},
            "valid": {"index": 2, "color": BLUE},
        },
    }
    store = ColorCycleStore(hass)
    await store.async_load()
    assert store.positions == {
        "valid": {key: {"index": 2, "color": BLUE} for key in PALETTE_GESTURES}
    }
    assert normalize_palette(PALETTE) == PALETTE


@pytest.mark.parametrize("key", PALETTE_GESTURES)
@pytest.mark.parametrize("scope", ["shared", "custom"])
async def test_each_gesture_palette_limit_and_validation(hass, key, scope):
    root = {"defaults": {}, "devices": [config()]}
    target = root["defaults"] if scope == "shared" else root["devices"][0]
    target["color_palettes"] = {key: [RED] * 25}
    parsed = await validate_document(hass, root)
    assert len(parsed[0].color_palettes[key]) == 25
    target["color_palettes"][key].append(BLUE)
    with pytest.raises(ValueError, match="between 1 and 25"):
        await validate_document(hass, root)


@pytest.mark.parametrize(
    "choices", [None, [], "default", {"on_tap": PALETTE}, {"stop_hold": []}]
)
async def test_invalid_gesture_palette_mapping_rejected(hass, choices):
    with pytest.raises(ValueError, match="color_palette"):
        await validate_document(
            hass, {"defaults": {"color_palettes": choices}, "devices": []}
        )


async def test_old_common_palettes_become_independent_without_losing_colors(hass):
    original = {
        "defaults": {"color_palette": PALETTE},
        "devices": [
            config(color_palette=[BLUE, WHITE], color_palettes={"stop_hold": [RED]})
        ],
    }
    snapshot = deepcopy(original)
    converted = migrate_palette_document(original)
    configs = await validate_document(hass, converted)
    assert converted["defaults"]["color_palettes"] == {
        key: PALETTE for key in PALETTE_GESTURES
    }
    assert configs[0].color_palettes == {
        "stop_tap": [BLUE, WHITE],
        "stop_hold": [RED],
        "stop_double_tap": [BLUE, WHITE],
    }
    converted["defaults"]["color_palettes"]["stop_tap"][0]["rgb_color"][0] = 1
    assert converted["defaults"]["color_palettes"]["stop_hold"] == PALETTE
    assert original == snapshot
    assert "color_palette" not in converted["devices"][0]


async def test_each_gesture_inherits_only_matching_shared_palette(hass):
    shared = {"color_palettes": {"stop_tap": [RED, BLUE], "stop_hold": [WHITE, RED]}}
    conf = parse_pico_config(
        hass, shared, config(color_palettes={"stop_tap": [BLUE]}), from_ui=True
    )
    assert conf.color_palettes == {
        "stop_tap": [BLUE],
        "stop_hold": [WHITE, RED],
        "stop_double_tap": DEFAULT_PALETTE,
    }
    conf.color_palettes["stop_hold"][0]["color_temp_kelvin"] = 3200
    assert shared["color_palettes"]["stop_hold"] == [WHITE, RED]
    other = parse_pico_config(
        hass, shared, config(color_palettes={"stop_tap": "default"}), from_ui=True
    )
    assert other.color_palettes["stop_tap"] == [RED, BLUE]


async def test_gestures_use_independent_colors_and_resume_after_restart(
    pico, hass_storage
):
    palettes = {
        "stop_tap": [RED, BLUE],
        "stop_hold": [WHITE, BLUE],
        "stop_double_tap": [BLUE, RED],
    }
    assert await pico.setup_ui(
        [config(**{key: "default" for key in PALETTE_GESTURES})],
        {
            **{key: "color_cycle" for key in PALETTE_GESTURES},
            "color_palettes": palettes,
            "double_tap_time_ms": 100,
        },
    )
    # Interleave real press/release recognition; a Hold must not consume Tap.
    for key, color in [
        ("stop_tap", RED),
        ("stop_hold", WHITE),
        ("stop_double_tap", BLUE),
        ("stop_tap", BLUE),
    ]:
        pico.fire("stop")
        if key == "stop_hold":
            await asyncio.sleep(0.14)
        pico.fire("stop", "release")
        if key == "stop_double_tap":
            pico.tap("stop")
        assert (await pico.next_call())[2] == {
            **color,
            "entity_id": ["light.a", "light.b"],
        }
        await pico.drain()
    store = get_cycle_store(pico.hass)
    device_id = next(iter(store.positions))
    expected = {
        "stop_tap": {"index": 1, "color": BLUE},
        "stop_hold": {"index": 0, "color": WHITE},
        "stop_double_tap": {"index": 0, "color": BLUE},
    }
    assert store.positions[device_id] == expected
    await pico.stop()
    pico.hass.bus.async_fire(EVENT_HOMEASSISTANT_FINAL_WRITE)
    await pico.drain()
    assert hass_storage[STORAGE_KEY]["data"][device_id] == expected
    restored = ColorCycleStore(pico.hass)
    await restored.async_load()
    for key, color in [
        ("stop_hold", BLUE),
        ("stop_double_tap", RED),
        ("stop_tap", RED),
    ]:
        await restored.async_cycle(device_id, key, ["light.other"], palettes[key])
        assert (await pico.next_call())[2] == {**color, "entity_id": ["light.other"]}
    # A changed Tap palette resets Tap only, leaving both saved sibling positions.
    siblings = {
        key: deepcopy(restored.positions[device_id][key])
        for key in ("stop_hold", "stop_double_tap")
    }
    restored.reconcile(device_id, "stop_tap", [WHITE])
    assert "stop_tap" not in restored.positions[device_id]
    assert restored.positions[device_id] == siblings


async def test_previous_common_position_resumes_independently(pico, hass_storage):
    hass_storage[STORAGE_KEY] = {
        "version": 1,
        "data": {"pico": {"index": 0, "color": RED}},
    }
    store = ColorCycleStore(pico.hass)
    await store.async_load()
    for key in PALETTE_GESTURES:
        await store.async_cycle("pico", key, ["light.a"], PALETTE)
        assert (await pico.next_call())[2] == {**WHITE, "entity_id": ["light.a"]}
    assert all(position["index"] == 1 for position in store.positions["pico"].values())
