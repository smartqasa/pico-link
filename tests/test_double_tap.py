"""Double taps through HA events, real timers, and recorded device commands."""

import asyncio
from copy import deepcopy

import pytest
from test_button_overrides import CASES, actions, config

from custom_components.pico_link.config import parse_pico_config


def scenes(pico):
    return [call[2]["entity_id"] for call in pico.calls if call[0] == "scene"]


@pytest.mark.parametrize("kind,button", CASES)
async def test_double_tap_on_every_button_replaces_both_single_taps(pico, kind, button):
    assert await pico.setup(
        [
            config(
                kind,
                **{
                    f"{button}_tap": actions("single"),
                    f"{button}_hold": actions("hold"),
                    f"{button}_double_tap": actions("double"),
                },
            )
        ]
    )
    pico.tap(button, kind=kind)
    await asyncio.sleep(0.025)
    assert pico.calls == []
    pico.fire(button, kind=kind)
    await asyncio.sleep(0.025)
    assert pico.calls == []  # The second press could still become a hold.
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert scenes(pico) == ["scene.double"]
    # HA's drain can return before cancelled-task completion callbacks run.
    await asyncio.sleep(0)
    assert all(not ctrl._tasks for ctrl in pico.hass.data["pico_link"]["controllers"])


@pytest.mark.parametrize("kind,button", CASES)
async def test_double_only_retains_normal_single_action(pico, kind, button):
    legacy = {"buttons": {button: actions("legacy")}} if kind == "4B" else {}
    if button == "stop":
        legacy = {"middle_button": actions("legacy")}
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup(
        [config(kind, **legacy, **{f"{button}_double_tap": actions("double")})],
        defaults={"double_tap_time_ms": 100},
    )
    pico.tap(button, kind=kind)
    await asyncio.sleep(0.025)
    assert pico.calls == []
    await pico.drain()
    assert len(pico.calls) == 1
    if kind == "4B" or button == "stop":
        assert scenes(pico) == ["scene.legacy"]
    else:
        assert pico.calls[0][0:2] == (
            "light",
            "turn_off" if button == "off" else "turn_on",
        )
        if button != "off":
            assert (
                pico.calls[0][2]["brightness_pct"]
                == {"on": 100, "raise": 60, "lower": 40}[button]
            )


@pytest.mark.parametrize("domain", ["light", "cover", "media_player"])
@pytest.mark.parametrize("kind", ["P2B", "2B", "2BRL", "3BRL"])
@pytest.mark.parametrize("second_press", [False, True])
async def test_native_hold_is_not_delayed_by_double_window(
    pico, domain, kind, second_press
):
    field = "media_players" if domain == "media_player" else f"{domain}s"
    entity = f"{domain}.test"
    pico.hass.states.async_set(
        entity, "on", {"brightness": 128, "current_position": 50, "volume_level": 0.5}
    )
    button = "raise" if kind in {"2BRL", "3BRL"} else "on"
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": kind,
                field: entity,
                f"{button}_double_tap": actions("double"),
                "double_tap_time_ms": 1500,
            }
        ]
    )
    if second_press:
        pico.tap(button, kind=kind)
        await asyncio.sleep(0.025)
    pico.fire(button, kind=kind)
    assert (await asyncio.wait_for(pico.next_call(), 0.3))[0] == domain
    if domain != "cover":
        await pico.next_call()
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert scenes(pico) == []
    if domain == "light":
        assert [c[2]["brightness_pct"] for c in pico.calls] == [60, 70]
    elif domain == "media_player":
        assert [c[2]["volume_level"] for c in pico.calls] == [0.6, 0.7]
    else:
        assert [c[1] for c in pico.calls] == ["open_cover", "stop_cover"]


@pytest.mark.parametrize("second_press", [False, True])
async def test_custom_hold_wins_once_without_later_single_or_double(pico, second_press):
    assert await pico.setup(
        [
            config(
                on_tap=actions("single"),
                on_hold=actions("hold"),
                on_double_tap=actions("double"),
            )
        ]
    )
    if second_press:
        pico.tap("on")
        await asyncio.sleep(0.025)
    pico.fire("on")
    assert (await pico.next_call())[2]["entity_id"] == "scene.hold"
    await asyncio.sleep(0.15)
    pico.fire("on", "release")
    await pico.drain()
    assert scenes(pico) == ["scene.hold"]
    # The held gesture must not seed the next double-tap pair.
    pico.tap("on")
    await pico.drain()
    assert scenes(pico) == ["scene.hold", "scene.single"]


async def test_default_window_starts_at_release_and_second_tap_can_finish_later(pico):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_double_tap=actions("double"),
                hold_time_ms=500,
            )
        ]
    )
    pico.fire("stop")
    await asyncio.sleep(0.2)
    pico.fire("stop", "release")
    await asyncio.sleep(0.2)
    assert pico.calls == []
    pico.fire("stop")  # 400ms since first press, but only 200ms since release.
    await asyncio.sleep(0.2)  # First release's 300ms deadline passes.
    assert pico.calls == []
    pico.fire("stop", "release")
    await pico.drain()
    assert scenes(pico) == ["scene.double"]


async def test_slow_taps_run_two_singles_and_new_pair_still_works(pico):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_double_tap=actions("double"),
                double_tap_time_ms=100,
            )
        ]
    )
    pico.tap("stop")
    await pico.next_call()
    pico.tap("stop")
    await pico.next_call()
    pico.tap("stop")
    pico.tap("stop")
    await pico.drain()
    assert scenes(pico) == ["scene.single", "scene.single", "scene.double"]


@pytest.mark.parametrize(
    "count,expected",
    [
        (3, ["scene.double", "scene.single"]),
        (4, ["scene.double", "scene.double"]),
    ],
)
async def test_rapid_taps_form_nonoverlapping_pairs(pico, count, expected):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_double_tap=actions("double"),
                double_tap_time_ms=100,
            )
        ]
    )
    for _ in range(count):
        pico.tap("stop")
    await pico.drain()
    assert scenes(pico) == expected


async def test_other_button_flushes_single_before_its_action_and_never_pairs(pico):
    assert await pico.setup(
        [
            config(
                on_double_tap=actions("double"),
                double_tap_time_ms=1000,
            )
        ]
    )
    pico.tap("on")
    await asyncio.sleep(0.025)
    assert pico.calls == []
    pico.tap("off")
    assert (await asyncio.wait_for(pico.next_call(), 0.2))[1] == "turn_on"
    assert (await pico.next_call())[1] == "turn_off"
    await pico.drain()
    assert len(pico.calls) == 2


async def test_different_double_enabled_buttons_do_not_pair(pico):
    assert await pico.setup(
        [
            config(
                on_tap=actions("on"),
                on_double_tap=actions("on_double"),
                off_tap=actions("off"),
                off_double_tap=actions("off_double"),
                double_tap_time_ms=100,
            )
        ]
    )
    pico.tap("on")
    pico.tap("off")
    await pico.drain()
    assert scenes(pico) == ["scene.on", "scene.off"]


@pytest.mark.parametrize("with_hold", [False, True])
async def test_unconfigured_buttons_keep_existing_response_time(pico, with_hold):
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup(
        [
            config(
                stop_double_tap=actions("double"),
                double_tap_time_ms=2000,
                **({"raise_hold": actions("hold")} if with_hold else {}),
            )
        ]
    )
    if with_hold:
        pico.tap("raise")
    else:
        pico.fire("raise")
    assert (await asyncio.wait_for(pico.next_call(), 0.08))[2]["brightness_pct"] == 60
    pico.fire("raise", "release")
    await pico.drain()
    assert len(pico.calls) == 1


async def test_timing_setting_alone_does_not_enable_double_tap(pico):
    assert await pico.setup([config(double_tap_time_ms=2000)])
    pico.tap("on")
    pico.tap("on")
    for _ in range(2):
        assert (await asyncio.wait_for(pico.next_call(), 0.08))[1] == "turn_on"
    await pico.drain()
    assert len(pico.calls) == 2


async def test_empty_double_list_consumes_double_but_keeps_single(pico):
    assert await pico.setup(
        [
            config(
                on_double_tap=[],
                double_tap_time_ms=100,
            )
        ]
    )
    pico.tap("on")
    pico.tap("on")
    await pico.drain()
    assert pico.calls == []
    pico.tap("on")
    await pico.drain()
    assert len(pico.calls) == 1 and pico.calls[0][1] == "turn_on"


@pytest.mark.parametrize("second_press", [False, True])
async def test_no_hold_action_long_press_runs_single_once(pico, second_press):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_double_tap=actions("double"),
            )
        ]
    )
    if second_press:
        pico.tap("stop")
        await asyncio.sleep(0.025)
    pico.fire("stop")
    assert (await pico.next_call())[2]["entity_id"] == "scene.single"
    await asyncio.sleep(0.15)
    pico.fire("stop", "release")
    await pico.drain()
    assert scenes(pico) == ["scene.single"]


async def test_empty_hold_still_suppresses_all_tap_actions(pico):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_hold=[],
                stop_double_tap=actions("double"),
            )
        ]
    )
    pico.tap("stop")
    pico.fire("stop")
    await asyncio.sleep(0.15)
    pico.fire("stop", "release")
    await pico.drain()
    assert pico.calls == []


async def test_duplicate_press_and_stray_release_do_not_invent_taps(pico):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_double_tap=actions("double"),
                double_tap_time_ms=100,
            )
        ]
    )
    pico.fire("stop", "release")
    pico.fire("stop")
    pico.fire("stop")
    pico.fire("stop", "release")
    pico.fire("stop", "release")
    await pico.drain()
    assert scenes(pico) == ["scene.single"]


@pytest.mark.parametrize("phase", ["first_press", "waiting", "second_press", "running"])
async def test_shutdown_cancels_all_pending_double_tap_work(pico, phase):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("script", "turn_on", wait)
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_double_tap=[{"action": "script.turn_on"}, *actions("last")],
            )
        ]
    )
    pico.fire("stop")
    if phase != "first_press":
        pico.fire("stop", "release")
    if phase in {"second_press", "running"}:
        pico.fire("stop")
    if phase == "running":
        pico.fire("stop", "release")
        assert (await pico.next_call())[0] == "script"
    else:
        await asyncio.sleep(0.025)
    await pico.stop()
    gate.set()
    pico.tap("stop")
    await pico.drain()
    assert [c[0] for c in pico.calls] == (["script"] if phase == "running" else [])


async def test_slow_double_action_does_not_block_four_other_remotes(pico):
    gate = asyncio.Event()

    async def wait(call):
        await gate.wait()

    pico.register("script", "turn_on", wait)
    devices = [
        config(
            device_id=f"pico{i}",
            stop_tap=actions(f"single{i}"),
            stop_double_tap=actions(f"double{i}"),
            double_tap_time_ms=100,
        )
        for i in range(5)
    ]
    devices[0]["stop_double_tap"] = [{"action": "script.turn_on"}, *actions("last")]
    assert await pico.setup(devices)
    pico.tap("stop", device="pico0")
    pico.tap("stop", device="pico0")
    assert (await pico.next_call())[0] == "script"
    for i in range(1, 5):
        pico.tap("stop", device=f"pico{i}")
        pico.tap("stop", device=f"pico{i}")
    for _ in range(4):
        assert (await asyncio.wait_for(pico.next_call(), 0.2))[0] == "scene"
    assert set(scenes(pico)) == {f"scene.double{i}" for i in range(1, 5)}
    gate.set()
    await pico.drain()
    assert scenes(pico)[-1] == "scene.last"
    assert all(not ctrl._tasks for ctrl in pico.hass.data["pico_link"]["controllers"])


@pytest.mark.parametrize("recognized", [False, True])
async def test_cover_stop_orders_pending_tap_or_double_and_newer_command(
    pico, recognized
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
                "stop_tap": actions("single"),
                "stop_double_tap": actions("double"),
            }
        ]
    )
    pico.fire("raise")
    await pico.next_call()
    await pico.next_call()
    pico.tap("stop")
    assert (await pico.next_call())[1] == "stop_cover"
    if recognized:
        pico.tap("stop")
    pico.tap("lower")
    pico.fire("raise", "release")
    await asyncio.sleep(0.03)
    assert scenes(pico) == []
    gate.set()
    await pico.drain()
    assert [c[1] for c in pico.calls] == [
        "set_cover_position",
        "open_cover",
        "stop_cover",
        "turn_on",
        "set_cover_position",
    ]
    assert scenes(pico) == ["scene.double" if recognized else "scene.single"]


@pytest.mark.parametrize("kind", ["P2B", "2B", "2BRL", "3BRL"])
async def test_cover_on_still_stops_movement_without_double_tap_delay(pico, kind):
    pico.hass.states.async_set("cover.test", "opening", {"current_position": 50})
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": kind,
                "covers": "cover.test",
                "on_double_tap": actions("double"),
                "double_tap_time_ms": 2000,
            }
        ]
    )
    pico.fire("on", kind=kind)
    assert (await asyncio.wait_for(pico.next_call(), 0.08))[1] == "stop_cover"
    pico.fire("on", "release", kind=kind)
    await pico.drain()
    assert [c[1] for c in pico.calls] == ["stop_cover"]


@pytest.mark.parametrize(
    "value,expected",
    [
        (-1, 100),
        (5000, 2000),
        ("450", 450),
        ("bad", 300),
        (None, 300),
        (True, 300),
        (0, 300),
    ],
)
async def test_double_window_uses_existing_timing_normalization(hass, value, expected):
    conf = parse_pico_config(hass, {}, config(double_tap_time_ms=value))
    assert conf.double_tap_time_ms == expected


async def test_shared_defaults_device_override_and_placeholders(hass):
    defaults = {
        "double_tap_time_ms": 600,
        "on_double_tap": [
            {"action": "light.turn_on", "target": {"entity_id": "lights"}}
        ],
    }
    original = deepcopy(defaults)
    conf = parse_pico_config(hass, {}, config())
    assert conf.double_tap_time_ms == 300
    conf = parse_pico_config(hass, defaults, config())
    assert conf.double_tap_time_ms == 600 and conf.hold_time_ms == 400
    assert conf.overrides["on_double_tap"][0]["target"]["entity_id"] == ["light.test"]
    conf = parse_pico_config(
        hass, defaults, config(double_tap_time_ms=450, on_double_tap=[])
    )
    assert conf.double_tap_time_ms == 450 and conf.overrides["on_double_tap"] == []
    assert defaults == original


@pytest.mark.parametrize(
    "kind,key,value",
    [
        ("3BRL", "on_double_tap", None),
        ("3BRL", "on_double_tap", {}),
        ("3BRL", "on_double_tap", ["bad"]),
        ("2B", "raise_double_tap", []),
        ("4B", "on_double_tap", []),
        ("3BRL", "middle_double_tap", []),
    ],
)
async def test_invalid_double_tap_configuration_is_rejected(hass, kind, key, value):
    with pytest.raises(ValueError, match=key):
        parse_pico_config(hass, {}, config(kind, **{key: value}))


async def test_expired_window_is_checked_even_without_timer_callback(pico):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_double_tap=actions("double"),
                double_tap_time_ms=100,
            )
        ]
    )
    pico.tap("stop")
    await asyncio.sleep(0.02)
    # Simulate a callback that never runs. Event handling must still enforce
    # the actual deadline rather than accepting any still-pending first tap.
    router = pico.hass.data["pico_link"]["controllers"][0]._overrides
    router.pending_tap.timer.cancel()
    await asyncio.sleep(0.12)
    pico.tap("stop")
    await pico.drain()
    assert scenes(pico) == ["scene.single", "scene.single"]


async def test_long_second_press_is_checked_even_without_hold_callback(pico):
    assert await pico.setup(
        [
            config(
                stop_tap=actions("single"),
                stop_hold=actions("hold"),
                stop_double_tap=actions("double"),
            )
        ]
    )
    pico.tap("stop")
    pico.fire("stop")
    await asyncio.sleep(0.02)
    router = pico.hass.data["pico_link"]["controllers"][0]._overrides
    router.timer.cancel()
    await asyncio.sleep(0.12)
    pico.fire("stop", "release")
    await pico.drain()
    assert scenes(pico) == ["scene.hold"]


async def test_waiting_single_tap_does_not_delay_another_remote(pico):
    assert await pico.setup(
        [
            config(
                device_id="waiting",
                on_double_tap=actions("double"),
                double_tap_time_ms=1500,
            ),
            config(device_id="immediate"),
        ]
    )
    pico.tap("on", device="waiting")
    await asyncio.sleep(0.02)
    assert pico.calls == []
    pico.tap("off", device="immediate")
    assert (await asyncio.wait_for(pico.next_call(), 0.1))[1] == "turn_off"
    await pico.drain()
    assert [c[1] for c in pico.calls] == ["turn_off", "turn_on"]


@pytest.mark.parametrize(
    "kind,button", [("P2B", "on"), ("2B", "on"), ("2BRL", "raise"), ("3BRL", "raise")]
)
async def test_double_override_retains_minimum_brightness_on_hold(pico, kind, button):
    pico.hass.states.async_set("light.test", "off")
    assert await pico.setup(
        [
            config(
                kind,
                light_low_pct=25,
                **{f"{button}_double_tap": actions("double")},
            )
        ]
    )
    pico.fire(button, kind=kind)
    assert (await pico.next_call())[2]["brightness_pct"] == 25
    assert (await pico.next_call())[2]["brightness_pct"] == 35
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert len(pico.calls) == 2
