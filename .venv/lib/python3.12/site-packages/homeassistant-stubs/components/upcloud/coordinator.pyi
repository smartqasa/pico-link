import upcloud_api
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class UpCloudDataUpdateCoordinator(DataUpdateCoordinator[dict[str, upcloud_api.Server]]):
    cloud_manager: Incomplete
    def __init__(self, hass: HomeAssistant, *, cloud_manager: upcloud_api.CloudManager, update_interval: timedelta, username: str) -> None: ...
    update_interval: Incomplete
    async def async_update_config(self, config_entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, upcloud_api.Server]: ...
