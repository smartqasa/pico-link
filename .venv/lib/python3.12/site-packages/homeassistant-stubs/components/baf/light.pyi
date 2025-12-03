from . import BAFConfigEntry as BAFConfigEntry
from .entity import BAFEntity as BAFEntity
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: BAFConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFLight(BAFEntity, LightEntity):
    _attr_name: Incomplete
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class BAFFanLight(BAFLight):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete

class BAFStandaloneLight(BAFLight):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    def __init__(self, device: Device) -> None: ...
    _attr_color_temp_kelvin: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
