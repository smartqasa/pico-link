"""Exercise optional overrides through real HA events, timers and service calls."""

import asyncio
from copy import deepcopy

import pytest

from custom_components.pico_link.config import parse_pico_config

BUTTONS = {
    "P2B": ["on", "off"],
    "2B": ["on", "off"],
    "2BRL": ["on", "off", "raise", "lower"],
    "3BRL": ["on", "off", "raise", "lower", "stop"],
    "4B": ["button_1", "button_2", "button_3", "off"],
}
CASES = [(kind, button) for kind, buttons in BUTTONS.items() for button in buttons]


def actions(name):
    return [{"action": "scene.turn_on", "target": {"entity_id": f"scene.{name}"}}]


def config(kind="3BRL", **options):
    return {
        "device_id": "pico",
        "type": kind,
        **({"lights": "light.test"} if kind != "4B" else {}),
        **options,
    }


@pytest.mark.parametrize("kind,button", CASES)
@pytest.mark.parametrize("hold", [False, True])
async def test_every_button_can_replace_tap_and_hold(pico, kind, button, hold):
    assert await pico.setup(
        [
            config(
                kind,
                **{f"{button}_tap": actions("tap"), f"{button}_hold": actions("hold")},
            )
        ]
    )
    pico.fire(button, kind=kind)
    if hold:
        assert (await pico.next_call())[2]["entity_id"] == "scene.hold"
        await asyncio.sleep(0.15)  # A long hold must not repeat.
    else:
        await asyncio.sleep(0.02)
        assert pico.calls == []
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert pico.calls == [
        ("scene", "turn_on", {"entity_id": "scene.hold" if hold else "scene.tap"})
    ]


@pytest.mark.parametrize("domain", ["light", "cover", "media_player"])
@pytest.mark.parametrize("kind", ["P2B", "2B", "2BRL", "3BRL"])
@pytest.mark.parametrize("up", [True, False])
async def test_tap_override_preserves_native_hold(pico, domain, kind, up):
    entity = f"{domain}.test"
    attrs = {"brightness": 128, "current_position": 50, "volume_level": 0.5}
    pico.hass.states.async_set(entity, "on", attrs)
    button = (
        ("raise" if up else "lower")
        if kind in {"2BRL", "3BRL"}
        else ("on" if up else "off")
    )
    field = "media_players" if domain == "media_player" else f"{domain}s"
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": kind,
                field: entity,
                f"{button}_tap": actions("tap"),
            }
        ]
    )
    pico.fire(button, kind=kind)
    await asyncio.sleep(0.025)
    assert pico.calls == []  # The competing tap must not run on press.
    first = await asyncio.wait_for(pico.next_call(), 0.15)  # No second hold delay.
    if domain != "cover":
        second = await pico.next_call()
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert all(call[0] == domain for call in pico.calls)
    if domain == "light":
        assert [call[2]["brightness_pct"] for call in pico.calls] == (
            [60, 70] if up else [40, 30]
        )
    elif domain == "media_player":
        assert [call[2]["volume_level"] for call in pico.calls] == (
            [0.6, 0.7] if up else [0.4, 0.3]
        )
    else:
        assert [call[1] for call in pico.calls] == [
            "open_cover" if up else "close_cover",
            "stop_cover",
        ]
    assert pico.calls[0] == first
    if domain != "cover":
        assert pico.calls[-1] == second


@pytest.mark.parametrize("kind,button", CASES)
async def test_hold_only_keeps_existing_tap(pico, kind, button):
    legacy = {"buttons": {button: actions("legacy")}} if kind == "4B" else {}
    if button == "stop":
        legacy = {"middle_button": actions("legacy")}
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup(
        [config(kind, **legacy, **{f"{button}_hold": actions("hold")})]
    )
    pico.tap(button, kind=kind)
    await pico.drain()
    if kind == "4B" or button == "stop":
        assert pico.calls == [("scene", "turn_on", {"entity_id": "scene.legacy"})]
    else:
        assert len(pico.calls) == 1
        assert pico.calls[0][0:2] == (
            "light",
            "turn_off" if button == "off" else "turn_on",
        )
        if button != "off":
            assert (
                pico.calls[0][2]["brightness_pct"]
                == {"on": 100, "raise": 60, "lower": 40}[button]
            )


@pytest.mark.parametrize("domain", ["light", "cover", "fan", "media_player", "switch"])
async def test_custom_hold_on_domains_without_default_on_hold(pico, domain):
    field = (
        "media_players"
        if domain == "media_player"
        else ("switches" if domain == "switch" else f"{domain}s")
    )
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                field: f"{domain}.test",
                "on_hold": actions("hold"),
            }
        ]
    )
    pico.fire("on")
    assert (await pico.next_call())[0] == "scene"
    pico.fire("on", "release")
    await pico.drain()
    assert len(pico.calls) == 1


@pytest.mark.parametrize("kind,button", [("3BRL", "stop"), ("4B", "button_1")])
async def test_explicit_tap_wins_over_legacy_and_runs_without_hold_delay(
    pico, kind, button
):
    legacy = (
        {"buttons": {button: actions("legacy")}}
        if kind == "4B"
        else {"middle_button": actions("legacy")}
    )
    assert await pico.setup(
        [config(kind, **legacy, **{f"{button}_tap": actions("tap")})]
    )
    pico.fire(button, kind=kind)
    assert (await asyncio.wait_for(pico.next_call(), 0.08))[2][
        "entity_id"
    ] == "scene.tap"
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert len(pico.calls) == 1


@pytest.mark.parametrize("hold", [False, True])
async def test_empty_override_disables_only_that_gesture(pico, hold):
    assert await pico.setup([config(raise_tap=[], raise_hold=[])])
    pico.fire("raise")
    if hold:
        await asyncio.sleep(0.15)
    pico.fire("raise", "release")
    pico.tap("on")
    await pico.drain()
    assert pico.calls == [
        ("light", "turn_on", {"entity_id": ["light.test"], "brightness_pct": 100})
    ]


async def test_new_native_press_cancels_pending_override_and_ignores_stale_release(
    pico,
):
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup([config(on_hold=actions("hold"))])
    pico.fire("on")
    await asyncio.sleep(0.02)
    pico.fire("lower")
    await pico.next_call()
    pico.fire("on", "release")
    await pico.next_call()
    pico.fire("lower", "release")
    await pico.drain()
    assert [call[2]["brightness_pct"] for call in pico.calls] == [40, 30]


async def test_custom_press_interrupts_native_ramp(pico):
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup([config(stop_tap=actions("stop"))])
    pico.fire("raise")
    await pico.next_call()
    await pico.next_call()
    pico.tap("stop")
    await pico.next_call()
    pico.fire("raise", "release")
    await pico.drain()
    assert [call[0] for call in pico.calls] == ["light", "light", "scene"]


async def test_rapid_native_taps_with_hold_override_accumulate(pico):
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup([config(raise_hold=actions("hold"))])
    for _ in range(3):
        pico.tap("raise")
    await pico.drain()
    assert [call[2]["brightness_pct"] for call in pico.calls] == [60, 70, 80]


async def test_custom_sequence_finishes_after_release_and_retains_order(pico):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("script", "turn_on", wait)
    assert await pico.setup(
        [config(on_hold=[{"action": "script.turn_on"}, *actions("last")])]
    )
    pico.fire("on")
    assert (await pico.next_call())[0] == "script"
    pico.fire("on", "release")
    await asyncio.sleep(0.02)
    assert len(pico.calls) == 1
    gate.set()
    await pico.drain()
    assert [call[0] for call in pico.calls] == ["script", "scene"]


async def test_five_remotes_are_independent_while_one_action_waits(pico):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("script", "turn_on", wait)
    devices = [
        config(
            device_id=f"pico{i}",
            stop_tap=actions(f"tap{i}"),
            stop_hold=actions(f"hold{i}"),
        )
        for i in range(5)
    ]
    devices[0]["stop_tap"] = [{"action": "script.turn_on"}, *actions("last")]
    assert await pico.setup(devices)
    pico.tap("stop", device="pico0")
    assert (await pico.next_call())[0] == "script"
    for i in range(1, 5):
        pico.fire("stop", device=f"pico{i}")
    for _ in range(4):
        assert (await pico.next_call())[0] == "scene"
    for i in range(1, 5):
        pico.fire("stop", "release", device=f"pico{i}")
    gate.set()
    await pico.drain()
    assert {call[2]["entity_id"] for call in pico.calls[1:]} == {
        "scene.last",
        "scene.hold1",
        "scene.hold2",
        "scene.hold3",
        "scene.hold4",
    }
    assert all(not ctrl._tasks for ctrl in pico.hass.data["pico_link"]["controllers"])


@pytest.mark.parametrize("recognized", [False, True])
async def test_shutdown_cancels_detection_and_running_sequences(pico, recognized):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("script", "turn_on", wait)
    assert await pico.setup(
        [config(on_hold=[{"action": "script.turn_on"}, *actions("last")])]
    )
    pico.fire("on")
    if recognized:
        await pico.next_call()
    else:
        await asyncio.sleep(0.02)
    await pico.stop()
    gate.set()
    pico.tap("on")
    await pico.drain()
    assert [call[0] for call in pico.calls] == (["script"] if recognized else [])


@pytest.mark.parametrize(
    "key,value",
    [
        ("on_tap", None),
        ("on_hold", {}),
        ("stop_hold", ["bad"]),
        ("middle_tap", []),
        ("button_1_hold", []),
        ("on_triple_tap", []),
        ("raise_tap", [{"action": "light.turn_on", "target": {"entity_id": [42]}}]),
    ],
)
async def test_invalid_overrides_are_rejected(hass, key, value):
    with pytest.raises(ValueError, match=key):
        parse_pico_config(hass, {}, config(**{key: value}))


async def test_defaults_placeholders_and_empty_override_are_copied(hass):
    defaults = {
        "on_tap": [{"action": "light.turn_on", "target": {"entity_id": "lights"}}],
        "off_hold": actions("default"),
    }
    original = deepcopy(defaults)
    conf = parse_pico_config(hass, defaults, config(off_hold=[]))
    assert conf.overrides["on_tap"][0]["target"]["entity_id"] == ["light.test"]
    assert conf.overrides["off_hold"] == []
    assert defaults == original


@pytest.mark.parametrize(
    "kind,key", [("P2B", "raise_tap"), ("2B", "stop_hold"), ("4B", "on_tap")]
)
async def test_override_must_match_physical_model(hass, kind, key):
    with pytest.raises(ValueError, match="supported button override"):
        parse_pico_config(hass, {}, config(kind, **{key: []}))


@pytest.mark.parametrize("next_button", ["stop", "lower"])
async def test_cover_stop_completes_before_custom_or_native_next_action(
    pico, next_button
):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("cover", "stop_cover", wait)
    pico.hass.states.async_set("cover.test", "open", {"current_position": 50})
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "covers": "cover.test",
                "stop_tap": actions("stop"),
            }
        ]
    )
    pico.fire("raise")
    await pico.next_call()  # Immediate step.
    await pico.next_call()  # Continuous motion.
    pico.tap("stop")
    assert (await pico.next_call())[1] == "stop_cover"
    if next_button == "lower":
        pico.tap("lower")
    pico.fire("raise", "release")
    await asyncio.sleep(0.03)
    assert [c[1] for c in pico.calls] == [
        "set_cover_position",
        "open_cover",
        "stop_cover",
    ]
    gate.set()
    await pico.drain()
    assert [c[1] for c in pico.calls] == [
        "set_cover_position",
        "open_cover",
        "stop_cover",
        "turn_on",
    ] + (["set_cover_position"] if next_button == "lower" else [])


async def test_cover_released_during_pending_stop_does_not_start_late_hold(pico):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("cover", "stop_cover", wait)
    pico.hass.states.async_set("cover.test", "open", {"current_position": 50})
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "covers": "cover.test",
                "lower_tap": actions("tap"),
            }
        ]
    )
    pico.fire("raise")
    await pico.next_call()
    await pico.next_call()
    pico.fire("lower")
    assert (await pico.next_call())[1] == "stop_cover"
    await asyncio.sleep(0.13)
    pico.fire("lower", "release")
    await asyncio.sleep(0.02)
    gate.set()
    await pico.drain()
    assert [c[1] for c in pico.calls] == [
        "set_cover_position",
        "open_cover",
        "stop_cover",
    ]


@pytest.mark.parametrize("kind", ["P2B", "2B", "2BRL", "3BRL"])
async def test_hold_override_keeps_cover_on_tap_stop_while_moving(pico, kind):
    pico.hass.states.async_set("cover.test", "opening", {"current_position": 50})
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": kind,
                "covers": "cover.test",
                "on_hold": actions("hold"),
            }
        ]
    )
    pico.tap("on", kind=kind)
    await pico.drain()
    assert [c[1] for c in pico.calls] == ["stop_cover"]


async def test_native_hold_keeps_cover_inversion(pico):
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "P2B",
                "covers": "cover.test",
                "cover_inverted": True,
                "on_tap": actions("tap"),
            }
        ]
    )
    pico.fire("on", kind="P2B")
    assert (await pico.next_call())[1] == "close_cover"
    pico.fire("on", "release", kind="P2B")
    await pico.drain()
    assert [c[1] for c in pico.calls] == ["close_cover", "stop_cover"]


@pytest.mark.parametrize(
    "kind,button", [("P2B", "on"), ("2B", "on"), ("2BRL", "raise"), ("3BRL", "raise")]
)
async def test_native_hold_retains_minimum_brightness_fix(pico, kind, button):
    pico.hass.states.async_set("light.test", "off")
    assert await pico.setup(
        [config(kind, light_low_pct=25, **{f"{button}_tap": actions("tap")})]
    )
    pico.fire(button, kind=kind)
    assert (await pico.next_call())[2]["brightness_pct"] == 25
    assert (await pico.next_call())[2]["brightness_pct"] == 35
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert len(pico.calls) == 2


@pytest.mark.parametrize("domain", ["light", "cover", "media_player"])
async def test_unconfigured_raise_still_responds_on_press_with_other_override(
    pico, domain
):
    pico.hass.states.async_set(
        f"{domain}.test",
        "on",
        {"brightness": 128, "current_position": 50, "volume_level": 0.5},
    )
    field = "media_players" if domain == "media_player" else f"{domain}s"
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                field: f"{domain}.test",
                "stop_hold": actions("hold"),
            }
        ]
    )
    pico.fire("raise")
    assert (await asyncio.wait_for(pico.next_call(), 0.08))[0] == domain
    pico.fire("raise", "release")
    await pico.drain()
    assert len(pico.calls) == 1


async def test_release_just_before_threshold_is_only_tap(pico):
    assert await pico.setup(
        [config(on_tap=actions("tap"), on_hold=actions("hold"))],
        defaults={"hold_time_ms": 200},
    )
    pico.fire("on")
    await asyncio.sleep(0.16)
    pico.fire("on", "release")
    await pico.drain()
    await asyncio.sleep(0.08)
    assert pico.calls == [("scene", "turn_on", {"entity_id": "scene.tap"})]


async def test_custom_service_failure_does_not_stop_later_actions(pico):
    async def fail(call):
        raise RuntimeError("unavailable test service")

    pico.register("script", "turn_on", fail)
    assert await pico.setup(
        [config(stop_tap=[{"action": "script.turn_on"}, *actions("last")])]
    )
    pico.tap("stop")
    await pico.drain()
    assert [c[0] for c in pico.calls] == ["script", "scene"]


async def test_new_override_cancels_unreleased_native_press_waiting_for_cover_stop(
    pico,
):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("cover", "stop_cover", wait)
    pico.hass.states.async_set("cover.test", "open", {"current_position": 50})
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "covers": "cover.test",
                "stop_tap": actions("stop"),
                "lower_tap": actions("lower"),
            }
        ]
    )
    pico.fire("raise")
    await pico.next_call()
    await pico.next_call()
    pico.tap("stop")
    await pico.next_call()
    pico.fire("raise")  # Queued behind the slow stop.
    pico.fire("lower")  # Supersedes that unreleased press.
    pico.fire("raise", "release")  # Its late release is stale.
    pico.fire("lower", "release")
    await asyncio.sleep(0.02)
    gate.set()
    await pico.drain()
    assert [c[1] for c in pico.calls] == [
        "set_cover_position",
        "open_cover",
        "stop_cover",
        "turn_on",
        "turn_on",
    ]
    assert [c[2]["entity_id"] for c in pico.calls[-2:]] == ["scene.stop", "scene.lower"]


async def test_shutdown_cancels_actions_waiting_for_cover_stop(pico):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("cover", "stop_cover", wait)
    pico.hass.states.async_set("cover.test", "open", {"current_position": 50})
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "covers": "cover.test",
                "stop_tap": actions("stop"),
            }
        ]
    )
    pico.fire("raise")
    await pico.next_call()
    await pico.next_call()
    pico.tap("stop")
    await pico.next_call()
    await pico.stop()
    gate.set()
    await pico.drain()
    assert [c[1] for c in pico.calls] == [
        "set_cover_position",
        "open_cover",
        "stop_cover",
    ]
