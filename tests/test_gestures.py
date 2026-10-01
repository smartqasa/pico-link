"""Real timer and event sequences that distinguish taps, holds and cancellation."""

import asyncio

import pytest

KINDS = ["P2B", "2B", "2BRL", "3BRL"]


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize("up", [True, False])
async def test_media_hold_changes_volume_without_tap_side_effects(pico, kind, up):
    pico.hass.states.async_set("media_player.test", "playing", {"volume_level": 0.5})
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, "media_players": "media_player.test"}]
    )
    button = (
        ("raise" if up else "lower")
        if kind in {"2BRL", "3BRL"}
        else ("on" if up else "off")
    )
    pico.fire(button, kind=kind)
    first = await pico.next_call()
    second = await pico.next_call()
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert pico.calls == [first, second]
    assert [service for _, service, _ in pico.calls] == ["volume_set", "volume_set"]
    assert [data["volume_level"] for _, _, data in pico.calls] == (
        [0.6, 0.7] if up else [0.4, 0.3]
    )


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize("up", [True, False])
async def test_cover_hold_moves_then_stops_on_release(pico, kind, up):
    pico.hass.states.async_set("cover.test", "open", {"current_position": 50})
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, "covers": "cover.test"}]
    )
    button = (
        ("raise" if up else "lower")
        if kind in {"2BRL", "3BRL"}
        else ("on" if up else "off")
    )
    pico.fire(button, kind=kind)
    if kind in {"2BRL", "3BRL"}:
        assert (await pico.next_call())[1:] == (
            "set_cover_position",
            {
                "entity_id": ["cover.test"],
                "position": 60 if up else 40,
            },
        )
    assert (await pico.next_call())[1] == ("open_cover" if up else "close_cover")
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert [service for _, service, _ in pico.calls] == (
        (["set_cover_position"] if kind in {"2BRL", "3BRL"} else [])
        + ["open_cover" if up else "close_cover", "stop_cover"]
    )


@pytest.mark.parametrize("kind", ["P2B", "2B"])
async def test_inverted_cover_hold_reverses_direction(pico, kind):
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": kind,
                "covers": "cover.test",
                "cover_inverted": True,
            }
        ]
    )
    pico.fire("on", kind=kind)
    assert (await pico.next_call())[1] == "close_cover"
    pico.fire("on", "release", kind=kind)
    await pico.drain()
    assert [service for _, service, _ in pico.calls] == ["close_cover", "stop_cover"]


@pytest.mark.parametrize("kind", KINDS)
async def test_light_downward_hold_stops_at_minimum_without_turning_off(pico, kind):
    pico.hass.states.async_set("light.test", "on", {"brightness": 204})
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": kind,
                "lights": "light.test",
                "light_low_pct": 25,
                "light_step_pct": 25,
            }
        ]
    )
    button = "lower" if kind in {"2BRL", "3BRL"} else "off"
    pico.fire(button, kind=kind)
    await pico.drain()  # The ramp must end naturally at its limit.
    pico.fire(button, "release", kind=kind)
    await pico.drain()
    assert [service for _, service, _ in pico.calls] == ["turn_on"] * 3
    assert [data["brightness_pct"] for _, _, data in pico.calls] == [55, 30, 25]


async def test_direction_change_ignores_the_old_buttons_release(pico):
    pico.hass.states.async_set("light.test", "on", {"brightness": 102})
    assert await pico.setup(
        [{"device_id": "pico", "type": "3BRL", "lights": "light.test"}]
    )
    pico.fire("raise")
    await pico.next_call()
    await pico.next_call()
    pico.fire("lower")
    await pico.next_call()
    pico.fire("raise", "release")  # This must not cancel LOWER's new hold.
    await pico.next_call()
    pico.fire("lower", "release")
    await pico.drain()
    assert [data["brightness_pct"] for _, _, data in pico.calls] == [50, 60, 50, 40]


async def test_holding_one_pico_does_not_block_another(pico):
    pico.hass.states.async_set("light.test", "on", {"brightness": 102})
    assert await pico.setup(
        [
            {"device_id": "pico", "type": "3BRL", "lights": "light.test"},
            {"device_id": "other", "type": "2B", "switches": "switch.test"},
        ]
    )
    pico.fire("raise")
    await pico.next_call()
    pico.tap("on", device="other", kind="2B")
    assert (await pico.next_call())[0:2] == ("switch", "turn_on")
    assert (await pico.next_call())[0:2] == ("light", "turn_on")
    pico.fire("raise", "release")
    await pico.drain()
    assert [domain for domain, _, _ in pico.calls] == ["light", "switch", "light"]


@pytest.mark.parametrize("domain,key", [("fan", "fans"), ("switch", "switches")])
async def test_tap_only_devices_do_not_repeat_when_held(pico, domain, key):
    assert await pico.setup(
        [{"device_id": "pico", "type": "2B", key: f"{domain}.test"}]
    )
    pico.fire("on", kind="2B")
    await pico.next_call()
    # Observe beyond the configured hold threshold, rather than releasing immediately.
    await asyncio.sleep(0.25)
    pico.fire("on", "release", kind="2B")
    await pico.drain()
    assert len(pico.calls) == 1


async def test_cover_direction_change_waits_for_stop_to_finish(pico):
    stopped = asyncio.Event()

    async def slow_stop(call):
        await stopped.wait()

    pico.register("cover", "stop_cover", slow_stop)
    pico.hass.states.async_set("cover.test", "open", {"current_position": 50})
    # Keep the new hold threshold long enough to inspect the stop/step sequence.
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "covers": "cover.test",
                "hold_time_ms": 500,
            }
        ]
    )
    pico.fire("raise")
    await pico.next_call()
    await pico.next_call()
    pico.fire("lower")
    assert (await pico.next_call())[1] == "stop_cover"
    assert [s for _, s, _ in pico.calls] == [
        "set_cover_position",
        "open_cover",
        "stop_cover",
    ]
    stopped.set()
    assert (await pico.next_call())[1:] == (
        "set_cover_position",
        {
            "entity_id": ["cover.test"],
            "position": 40,
        },
    )
    pico.fire("lower", "release")
    await pico.drain()
    assert len(pico.calls) == 4
