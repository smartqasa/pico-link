import RFXtrx as rfxtrxmod
from . import DeviceTuple as DeviceTuple, async_setup_platform_entry as async_setup_platform_entry
from .const import COMMAND_OFF_LIST as COMMAND_OFF_LIST, COMMAND_ON_LIST as COMMAND_ON_LIST
from .entity import RfxtrxCommandEntity as RfxtrxCommandEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

def supported(event: rfxtrxmod.RFXtrxEvent) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RfxtrxLight(RfxtrxCommandEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_brightness: int
    _device: rfxtrxmod.LightingDevice
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _apply_event(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    @callback
    def _handle_event(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> None: ...
