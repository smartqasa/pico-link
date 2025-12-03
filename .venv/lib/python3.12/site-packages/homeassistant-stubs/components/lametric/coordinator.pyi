from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from demetriek import Device
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class LaMetricDataUpdateCoordinator(DataUpdateCoordinator[Device]):
    config_entry: ConfigEntry
    lametric: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> Device: ...
