"""The 2BRL profile: a 3BRL without the Stop button."""

import pytest

from custom_components.pico_link.config import parse_pico_config


async def test_2brl_steps_and_ramps_like_a_3brl(pico):
    """On, Off, Raise and Lower behave exactly as they do on a 3BRL."""
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup(
        [{"device_id": "pico", "type": "2BRL", "lights": "light.test"}]
    )

    pico.fire("raise", kind="2BRL")
    assert (await pico.next_call())[1:] == (
        "turn_on",
        {"entity_id": ["light.test"], "brightness_pct": 60},
    )
    pico.fire("raise", "release", kind="2BRL")
    await pico.drain()

    pico.calls.clear()
    pico.fire("off", kind="2BRL")
    assert (await pico.next_call())[1] == "turn_off"
    pico.fire("off", "release", kind="2BRL")
    await pico.drain()


async def test_2brl_has_no_stop_button(pico):
    """A stop event is ignored rather than mapped onto another action."""
    pico.hass.states.async_set("light.test", "on", {"brightness": 128})
    assert await pico.setup(
        [{"device_id": "pico", "type": "2BRL", "lights": "light.test"}]
    )

    pico.fire("stop", kind="2BRL")
    pico.fire("stop", "release", kind="2BRL")
    await pico.drain()

    assert pico.calls == []


@pytest.mark.parametrize(
    "key,error",
    [
        ("middle_button", "only valid for 3BRL"),
        ("stop_tap", "not a supported button override"),
        ("stop_hold", "not a supported button override"),
        ("stop_double_tap", "not a supported button override"),
    ],
)
async def test_2brl_rejects_stop_configuration(hass, key, error):
    """Stop actions need a Stop button, so configuring one is an error."""
    with pytest.raises(ValueError, match=error):
        parse_pico_config(
            hass,
            {},
            {
                "device_id": "pico",
                "type": "2BRL",
                "lights": "light.desk",
                key: [{"action": "light.turn_on", "target": {"entity_id": "light.x"}}],
            },
        )
