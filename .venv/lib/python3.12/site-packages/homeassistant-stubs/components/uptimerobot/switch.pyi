from .const import API_ATTR_OK as API_ATTR_OK, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from .entity import UptimeRobotEntity as UptimeRobotEntity
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UptimeRobotSwitch(UptimeRobotEntity, SwitchEntity):
    _attr_translation_key: str
    @property
    def is_on(self) -> bool: ...
    async def _async_edit_monitor(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
