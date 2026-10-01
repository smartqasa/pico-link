"""A picker-visible placeholder, never a proxy for a real light service call."""

from homeassistant.components.light import ColorMode, LightEntity, LightEntityFeature
from homeassistant.exceptions import ServiceValidationError

from .placeholder import NAME, UNIQUE_ID


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Provide one shared placeholder without requiring a UI configuration entry."""
    async_add_entities([PicoLinkPlaceholder()])


class PicoLinkPlaceholder(LightEntity):
    """Advertise editor capabilities; Pico Link substitutes the target itself."""

    _attr_unique_id = UNIQUE_ID
    _attr_name = NAME
    _attr_icon = "mdi:lightbulb-auto-outline"
    _attr_should_poll = False
    _attr_is_on = False
    _attr_brightness = 255
    _attr_color_mode = ColorMode.RGB
    _attr_rgb_color = (255, 255, 255)
    _attr_supported_color_modes = {
        ColorMode.COLOR_TEMP,
        ColorMode.HS,
        ColorMode.RGB,
        ColorMode.RGBW,
        ColorMode.RGBWW,
        ColorMode.XY,
    }
    _attr_min_color_temp_kelvin = 1000
    _attr_max_color_temp_kelvin = 40000
    _attr_supported_features = (
        LightEntityFeature.TRANSITION
        | LightEntityFeature.FLASH
        | LightEntityFeature.EFFECT
    )
    # Effect names depend on the eventual real lights. Do not invent presets.
    _attr_effect_list = []

    async def async_turn_on(self, **kwargs):
        raise ServiceValidationError(
            "Pico Link placeholder requires a triggering Pico. "
            "Use it in a Pico Link button action and test with the remote."
        )

    async def async_turn_off(self, **kwargs):
        await self.async_turn_on(**kwargs)
