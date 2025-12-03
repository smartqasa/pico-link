from _typeshed import Incomplete
from homeassistant.components.humidifier import HumidifierAction as HumidifierAction, HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityFeature as HumidifierEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SUPPORT_FLAGS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoHumidifier(HumidifierEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_is_on: Incomplete
    _attr_action: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_humidity: Incomplete
    _attr_current_humidity: Incomplete
    _attr_mode: Incomplete
    _attr_available_modes: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, name: str, mode: str | None, target_humidity: float, current_humidity: float | None = None, available_modes: list[str] | None = None, is_on: bool = True, action: HumidifierAction | None = None, device_class: HumidifierDeviceClass | None = None) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
