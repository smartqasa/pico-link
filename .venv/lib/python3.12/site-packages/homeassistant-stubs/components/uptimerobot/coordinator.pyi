from .const import API_ATTR_OK as API_ATTR_OK, COORDINATOR_UPDATE_INTERVAL as COORDINATOR_UPDATE_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyuptimerobot import UptimeRobot as UptimeRobot, UptimeRobotMonitor

class UptimeRobotDataUpdateCoordinator(DataUpdateCoordinator[list[UptimeRobotMonitor]]):
    config_entry: ConfigEntry
    _config_entry_id: Incomplete
    _device_registry: Incomplete
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry_id: str, dev_reg: dr.DeviceRegistry, api: UptimeRobot) -> None: ...
    async def _async_update_data(self) -> list[UptimeRobotMonitor]: ...
