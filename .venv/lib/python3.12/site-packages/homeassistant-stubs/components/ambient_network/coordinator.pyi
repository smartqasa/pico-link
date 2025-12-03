from .const import API_LAST_DATA as API_LAST_DATA, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helper import get_station_name as get_station_name
from _typeshed import Incomplete
from aioambient import OpenAPI as OpenAPI
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

SCAN_INTERVAL: Incomplete

class AmbientNetworkDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: ConfigEntry
    station_name: str
    last_measured: datetime | None
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: OpenAPI) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
