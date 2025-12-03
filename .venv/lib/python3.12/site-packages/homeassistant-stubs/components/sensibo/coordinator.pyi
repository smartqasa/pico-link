from . import SensiboConfigEntry as SensiboConfigEntry
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER, TIMEOUT as TIMEOUT
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysensibo.model import SensiboData

REQUEST_REFRESH_DELAY: float

class SensiboDataUpdateCoordinator(DataUpdateCoordinator[SensiboData]):
    config_entry: SensiboConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SensiboConfigEntry) -> None: ...
    async def _async_update_data(self) -> SensiboData: ...
