from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SCAN_INTERVAL: Incomplete
type StookwijzerConfigEntry = ConfigEntry[StookwijzerCoordinator]

class StookwijzerCoordinator(DataUpdateCoordinator[None]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: StookwijzerConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
