from .const import CONF_APP_ID as CONF_APP_ID, POLLING_PERIOD_S as POLLING_PERIOD_S
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from ttn_client import TTNClient

_LOGGER: Incomplete

class TTNCoordinator(DataUpdateCoordinator[TTNClient.DATA_TYPE]):
    _client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> TTNClient.DATA_TYPE: ...
    async def _push_callback(self, data: TTNClient.DATA_TYPE) -> None: ...
