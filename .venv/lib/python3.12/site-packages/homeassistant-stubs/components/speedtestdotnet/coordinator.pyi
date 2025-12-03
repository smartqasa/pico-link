import speedtest
from .const import CONF_SERVER_ID as CONF_SERVER_ID, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_SERVER as DEFAULT_SERVER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

class SpeedTestDataCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: ConfigEntry
    hass: Incomplete
    api: Incomplete
    servers: dict[str, dict]
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, api: speedtest.Speedtest) -> None: ...
    def update_servers(self) -> None: ...
    def update_data(self) -> dict[str, Any]: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
