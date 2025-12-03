from .const import CONF_STATION_NUMBER as CONF_STATION_NUMBER, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiowaqi import WAQIAirQuality, WAQIClient as WAQIClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class WAQIDataUpdateCoordinator(DataUpdateCoordinator[WAQIAirQuality]):
    config_entry: ConfigEntry
    _client: Incomplete
    def __init__(self, hass: HomeAssistant, client: WAQIClient) -> None: ...
    async def _async_update_data(self) -> WAQIAirQuality: ...
