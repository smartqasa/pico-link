from . import AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from .entity import AbodeDevice as AbodeDevice
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, DEFAULT_MAX_KELVIN as DEFAULT_MAX_KELVIN, DEFAULT_MIN_KELVIN as DEFAULT_MIN_KELVIN, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jaraco.abode.devices.light import Light as Light
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeLight(AbodeDevice, LightEntity):
    _device: Light
    _attr_name: Incomplete
    _attr_max_color_temp_kelvin = DEFAULT_MAX_KELVIN
    _attr_min_color_temp_kelvin = DEFAULT_MIN_KELVIN
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def color_mode(self) -> str | None: ...
    @property
    def supported_color_modes(self) -> set[str] | None: ...
