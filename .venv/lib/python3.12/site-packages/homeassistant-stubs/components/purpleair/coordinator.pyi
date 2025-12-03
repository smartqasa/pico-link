from .const import CONF_SENSOR_INDICES as CONF_SENSOR_INDICES, LOGGER as LOGGER
from _typeshed import Incomplete
from aiopurpleair.models.sensors import GetSensorsResponse
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SENSOR_FIELDS_TO_RETRIEVE: Incomplete
UPDATE_INTERVAL: Incomplete

class PurpleAirDataUpdateCoordinator(DataUpdateCoordinator[GetSensorsResponse]):
    _entry: Incomplete
    _api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> GetSensorsResponse: ...
    @callback
    def async_get_map_url(self, sensor_index: int) -> str: ...
