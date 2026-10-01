"""User-visible commands for all supported non-scene Pico/device combinations."""

import pytest

KINDS = ["P2B", "2B", "2BRL", "3BRL"]


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "domain,key,button,service,data,options",
    [
        (
            "light",
            "lights",
            "on",
            "turn_on",
            {"brightness_pct": 80, "transition": 2},
            {"light_on_pct": 80, "light_transition_on": 2},
        ),
        (
            "light",
            "lights",
            "off",
            "turn_off",
            {"transition": 3},
            {"light_transition_off": 3},
        ),
        (
            "cover",
            "covers",
            "on",
            "set_cover_position",
            {"position": 75},
            {"cover_open_pos": 75},
        ),
        ("cover", "covers", "off", "close_cover", {}, {}),
        ("fan", "fans", "on", "set_percentage", {"percentage": 50}, {"fan_on_pct": 50}),
        ("fan", "fans", "off", "turn_off", {}, {}),
        ("media_player", "media_players", "on", "media_play_pause", {}, {}),
        ("media_player", "media_players", "off", "media_next_track", {}, {}),
        ("switch", "switches", "on", "turn_on", {}, {}),
        ("switch", "switches", "off", "turn_off", {}, {}),
    ],
)
async def test_on_off_taps(pico, kind, domain, key, button, service, data, options):
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, key: f"{domain}.test", **options}]
    )
    pico.tap(button, kind=kind)
    await pico.drain()
    assert pico.calls == [(domain, service, {"entity_id": [f"{domain}.test"], **data})]


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "button,service", [("on", "close_cover"), ("off", "open_cover")]
)
async def test_inverted_cover_taps(pico, kind, button, service):
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
    pico.tap(button, kind=kind)
    await pico.drain()
    assert pico.calls == [("cover", service, {"entity_id": ["cover.test"]})]


@pytest.mark.parametrize(
    "button,position,expected",
    [
        ("raise", 95, 100),
        ("lower", 5, 0),
        ("raise", 100, None),
        ("lower", 0, None),
    ],
)
@pytest.mark.parametrize("kind", ["2BRL", "3BRL"])
async def test_cover_steps_respect_endpoints(pico, kind, button, position, expected):
    pico.hass.states.async_set("cover.test", "open", {"current_position": position})
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, "covers": "cover.test"}]
    )
    pico.tap(button, kind=kind)
    await pico.drain()
    assert pico.calls == (
        []
        if expected is None
        else [
            (
                "cover",
                "set_cover_position",
                {"entity_id": ["cover.test"], "position": expected},
            )
        ]
    )


@pytest.mark.parametrize("kind", ["2BRL", "3BRL"])
async def test_rapid_cover_steps_accumulate_without_state_feedback(pico, kind):
    pico.hass.states.async_set("cover.test", "open", {"current_position": 20})
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, "covers": "cover.test"}]
    )
    for _ in range(3):
        pico.tap("raise", kind=kind)
    await pico.drain()
    assert [data["position"] for _, _, data in pico.calls] == [30, 40, 50]
    assert pico.hass.states.get("cover.test").attributes["current_position"] == 20


@pytest.mark.parametrize("kind", KINDS)
async def test_cover_on_while_moving_stops(pico, kind):
    pico.hass.states.async_set("cover.test", "opening", {"current_position": 20})
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, "covers": "cover.test"}]
    )
    pico.tap("on", kind=kind)
    await pico.drain()
    assert pico.calls == [("cover", "stop_cover", {"entity_id": ["cover.test"]})]


@pytest.mark.parametrize(
    "state,speed,step,button,expected",
    [
        ("off", 75, 25, "raise", 25),
        ("on", 25, 25, "raise", 50),
        ("on", 50, 25, "lower", 25),
        ("on", 100, 25, "raise", None),
        ("off", 0, 25, "lower", None),
        ("on", 25, 25, "lower", 0),
        ("off", 0, None, "raise", 100),
        ("off", 0, 0, "raise", 100),
    ],
)
@pytest.mark.parametrize("kind", ["2BRL", "3BRL"])
async def test_fan_speed_steps(pico, kind, state, speed, step, button, expected):
    pico.hass.states.async_set(
        "fan.test", state, {"percentage": speed, "percentage_step": step}
    )
    assert await pico.setup([{"device_id": "pico", "type": kind, "fans": "fan.test"}])
    pico.tap(button, kind=kind)
    await pico.drain()
    assert pico.calls == (
        []
        if expected is None
        else [
            (
                "fan",
                "set_percentage",
                {"entity_id": ["fan.test"], "percentage": expected},
            )
        ]
    )


@pytest.mark.parametrize(
    "direction,expected", [("forward", "reverse"), ("reverse", "forward"), (None, None)]
)
async def test_fan_middle_button_reverses_known_direction(pico, direction, expected):
    pico.hass.states.async_set("fan.test", "on", {"direction": direction})
    assert await pico.setup([{"device_id": "pico", "type": "3BRL", "fans": "fan.test"}])
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == (
        []
        if expected is None
        else [
            ("fan", "set_direction", {"entity_id": ["fan.test"], "direction": expected})
        ]
    )


@pytest.mark.parametrize(
    "button,volume,expected",
    [
        ("raise", 0.95, 1.0),
        ("lower", 0.05, 0.0),
        ("raise", 1.0, None),
        ("lower", 0.0, None),
        ("raise", None, None),
    ],
)
@pytest.mark.parametrize("kind", ["2BRL", "3BRL"])
async def test_volume_steps_respect_limits_and_missing_volume(
    pico, kind, button, volume, expected
):
    pico.hass.states.async_set("media_player.test", "playing", {"volume_level": volume})
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, "media_players": "media_player.test"}]
    )
    pico.tap(button, kind=kind)
    await pico.drain()
    assert pico.calls == (
        []
        if expected is None
        else [
            (
                "media_player",
                "volume_set",
                {"entity_id": ["media_player.test"], "volume_level": expected},
            )
        ]
    )


@pytest.mark.parametrize("muted", [True, False])
async def test_media_middle_button_toggles_mute(pico, muted):
    pico.hass.states.async_set(
        "media_player.test", "playing", {"is_volume_muted": muted}
    )
    assert await pico.setup(
        [{"device_id": "pico", "type": "3BRL", "media_players": "media_player.test"}]
    )
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == [
        (
            "media_player",
            "volume_mute",
            {
                "entity_id": ["media_player.test"],
                "is_volume_muted": not muted,
            },
        )
    ]


@pytest.mark.parametrize("button", ["raise", "lower", "stop"])
@pytest.mark.parametrize("kind", ["2BRL", "3BRL"])
async def test_switch_ignores_unsupported_buttons(pico, kind, button):
    assert await pico.setup(
        [{"device_id": "pico", "type": kind, "switches": "switch.test"}]
    )
    pico.tap(button, kind=kind)
    await pico.drain()
    assert pico.calls == []
