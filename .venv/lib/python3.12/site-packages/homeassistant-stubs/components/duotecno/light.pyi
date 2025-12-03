from .const import DOMAIN as DOMAIN
from .entity import DuotecnoEntity as DuotecnoEntity, api_call as api_call
from _typeshed import Incomplete
from duotecno.controller import PyDuotecno as PyDuotecno
from duotecno.unit import DimUnit as DimUnit
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DuotecnoLight(DuotecnoEntity, LightEntity):
    _unit: DimUnit
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @api_call
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_turn_off(self, **kwargs: Any) -> None: ...
