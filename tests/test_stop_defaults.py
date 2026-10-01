"""Stop defaults are opt-in, with the legacy middle-button name preserved."""

import asyncio
from copy import deepcopy

import pytest
from test_button_overrides import actions, config

from custom_components.pico_link.config import parse_pico_config

STOP_KEYS = ("stop_tap", "stop_double_tap", "stop_hold")


@pytest.mark.parametrize("kind", ["P2B", "2B", "3BRL", "4B"])
async def test_shared_stop_gestures_are_inactive_without_opt_in(hass, kind):
    raw = config(kind, off_tap=actions("off"))
    defaults = {key: actions(key) for key in STOP_KEYS}
    parsed = parse_pico_config(hass, defaults, raw)
    assert parsed.overrides == {"off_tap": actions("off")}


@pytest.mark.parametrize("kind", ["P2B", "2B", "4B"])
@pytest.mark.parametrize("key", STOP_KEYS)
async def test_stop_opt_in_on_unsupported_model_still_rejected(hass, kind, key):
    with pytest.raises(ValueError, match="not a supported button override"):
        parse_pico_config(
            hass, {key: actions("shared")}, config(kind, **{key: "default"})
        )


@pytest.mark.parametrize("key", STOP_KEYS)
@pytest.mark.parametrize("replacement", ["default", [], actions("local")])
async def test_each_stop_gesture_can_opt_in_replace_or_disable(hass, key, replacement):
    defaults = {name: actions(name) for name in STOP_KEYS}
    raw = config(**{key: replacement})
    original = deepcopy((defaults, raw))
    parsed = parse_pico_config(hass, defaults, raw)
    expected = defaults[key] if replacement == "default" else replacement
    assert parsed.overrides == {key: expected}
    assert (defaults, raw) == original


async def test_shared_stop_placeholders_are_resolved_for_each_opted_in_remote(hass):
    defaults = {
        key: [{"action": "light.turn_on", "target": {"entity_id": "lights"}}]
        for key in STOP_KEYS
    }
    original = deepcopy(defaults)
    for name in ("kitchen", "bedroom"):
        parsed = parse_pico_config(
            hass,
            defaults,
            config(lights=f"light.{name}", **dict.fromkeys(STOP_KEYS, "default")),
        )
        assert parsed.middle_button == []
        for key in STOP_KEYS:
            assert parsed.overrides[key][0]["target"]["entity_id"] == [f"light.{name}"]
    assert defaults == original


@pytest.mark.parametrize("key", STOP_KEYS)
async def test_missing_stop_default_disables_only_requested_gesture(hass, key):
    parsed = parse_pico_config(hass, {}, config(**{key: "default"}))
    assert parsed.overrides == {key: []}


@pytest.mark.parametrize("gesture", ["tap", "hold", "double_tap"])
async def test_unconfigured_shared_gestures_run_nothing(pico, gesture):
    assert await pico.setup(
        [
            config(
                middle_button=actions("legacy"), **dict.fromkeys(STOP_KEYS, "default")
            )
        ],
        defaults={"double_tap_time_ms": 100},
    )
    assert len(pico.hass.data["pico_link"]["controllers"]) == 1
    pico.fire("stop")
    if gesture == "hold":
        await asyncio.sleep(0.15)
    pico.fire("stop", "release")
    if gesture == "double_tap":
        await asyncio.sleep(0.02)
        pico.tap("stop")
    await asyncio.sleep(0.15)
    await pico.drain()
    assert pico.calls == []


@pytest.mark.parametrize(
    "field,domain,service",
    [
        ("covers", "cover", "stop_cover"),
        ("fans", "fan", "set_direction"),
        ("media_players", "media_player", "volume_mute"),
    ],
)
@pytest.mark.parametrize("device_key", ["stop_tap", "middle_button"])
@pytest.mark.parametrize("defaults", [{}, {"stop_tap": []}])
async def test_shared_do_nothing_does_not_disable_native_remotes(
    pico, field, domain, service, device_key, defaults
):
    entity = f"{domain}.test"
    pico.hass.states.async_set(
        entity, "on", {"direction": "forward", "is_volume_muted": False}
    )
    assert await pico.setup(
        [
            {
                "device_id": "shared",
                "type": "3BRL",
                field: entity,
                device_key: "default",
            },
            {"device_id": "normal", "type": "3BRL", field: entity},
        ],
        defaults=defaults,
    )
    assert len(pico.hass.data["pico_link"]["controllers"]) == 2
    pico.tap("stop", device="shared")
    await pico.drain()
    assert pico.calls == []
    pico.tap("stop", device="normal")
    await pico.drain()
    assert len(pico.calls) == 1
    assert pico.calls[0][:2] == (domain, service)


@pytest.mark.parametrize("key", STOP_KEYS)
async def test_invalid_stop_default_is_validated_when_requested(hass, key):
    with pytest.raises(ValueError, match="must be a list of actions"):
        parse_pico_config(hass, {key: "default"}, config(**{key: "default"}))


async def test_unknown_shared_button_is_not_silently_ignored(hass):
    with pytest.raises(ValueError, match="not a supported button override"):
        parse_pico_config(hass, {"stpo_tap": actions("typo")}, config("2B"))


@pytest.mark.parametrize("gesture", ["tap", "double_tap", "hold"])
async def test_opted_in_stop_gestures_work_in_mixed_model_setup(pico, gesture):
    defaults = {key: actions(key) for key in STOP_KEYS}
    defaults["double_tap_time_ms"] = 100
    assert await pico.setup(
        [
            config(device_id="five", **dict.fromkeys(STOP_KEYS, "default")),
            config("P2B", device_id="paddle"),
            config("2B", device_id="two"),
            config("4B", device_id="scene", off_tap=actions("scene_off")),
            config(device_id="unchanged", middle_button=actions("legacy")),
        ],
        defaults=defaults,
    )
    assert len(pico.hass.data["pico_link"]["controllers"]) == 5
    if gesture == "hold":
        pico.fire("stop", device="five")
        assert (await pico.next_call())[2]["entity_id"] == "scene.stop_hold"
        await asyncio.sleep(0.12)
        pico.fire("stop", "release", device="five")
    else:
        pico.tap("stop", device="five")
        if gesture == "double_tap":
            await asyncio.sleep(0.02)
            pico.tap("stop", device="five")
    await pico.drain()
    assert pico.calls == [("scene", "turn_on", {"entity_id": f"scene.stop_{gesture}"})]
    for kind, device in (("P2B", "paddle"), ("2B", "two"), ("4B", "scene")):
        pico.tap("off", kind=kind, device=device)
        await pico.drain()
    pico.tap("stop", device="unchanged")
    await pico.drain()
    assert pico.calls[1:] == [
        ("light", "turn_off", {"entity_id": ["light.test"]}),
        ("light", "turn_off", {"entity_id": ["light.test"]}),
        ("scene", "turn_on", {"entity_id": "scene.scene_off"}),
        ("scene", "turn_on", {"entity_id": "scene.legacy"}),
    ]


@pytest.mark.parametrize("legacy", ["default", actions("legacy")])
async def test_opted_in_double_and_hold_preserve_legacy_single_tap(pico, legacy):
    assert await pico.setup(
        [config(middle_button=legacy, stop_double_tap="default", stop_hold="default")],
        defaults={
            "middle_button": actions("legacy"),
            "stop_double_tap": actions("double"),
            "stop_hold": actions("hold"),
            "double_tap_time_ms": 100,
        },
    )
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == [("scene", "turn_on", {"entity_id": "scene.legacy"})]


@pytest.mark.parametrize("device_key", ["middle_button", "stop_tap"])
@pytest.mark.parametrize("default_key", ["middle_button", "stop_tap"])
async def test_both_tap_names_can_use_either_shared_tap_name(
    pico, device_key, default_key
):
    assert await pico.setup(
        [config(**{device_key: "default"})],
        defaults={default_key: actions("shared")},
    )
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == [("scene", "turn_on", {"entity_id": "scene.shared"})]


@pytest.mark.parametrize("device_key", ["middle_button", "stop_tap"])
async def test_new_shared_tap_name_wins_when_both_defaults_exist(pico, device_key):
    assert await pico.setup(
        [config(**{device_key: "default"})],
        defaults={"middle_button": actions("legacy"), "stop_tap": actions("new")},
    )
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == [("scene", "turn_on", {"entity_id": "scene.new"})]


@pytest.mark.parametrize("replacement", [[], actions("shared")])
async def test_opted_in_stop_tap_takes_precedence_over_local_middle_button(
    pico, replacement
):
    assert await pico.setup(
        [config(middle_button=actions("legacy"), stop_tap="default")],
        defaults={"stop_tap": replacement},
    )
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == (
        [("scene", "turn_on", {"entity_id": "scene.shared"})] if replacement else []
    )
