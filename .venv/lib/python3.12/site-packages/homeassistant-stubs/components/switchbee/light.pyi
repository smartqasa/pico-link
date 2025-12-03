from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBeeCoordinator as SwitchBeeCoordinator
from .entity import SwitchBeeDeviceEntity as SwitchBeeDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from switchbee.device import SwitchBeeDimmer
from typing import Any

MAX_BRIGHTNESS: int

def _hass_brightness_to_switchbee(value: int) -> int: ...
def _switchbee_brightness_to_hass(value: int) -> int: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitchBeeLightEntity(SwitchBeeDeviceEntity[SwitchBeeDimmer], LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_is_on: bool
    _attr_brightness: int
    def __init__(self, device: SwitchBeeDimmer, coordinator: SwitchBeeCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    def _update_attrs_from_coordinator(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
