from . import TVWeatherConfigEntry as TVWeatherConfigEntry
from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytrafikverket.models import WeatherStationInfoModel

_LOGGER: Incomplete
TIME_BETWEEN_UPDATES: Incomplete

class TVDataUpdateCoordinator(DataUpdateCoordinator[WeatherStationInfoModel]):
    config_entry: TVWeatherConfigEntry
    _weather_api: Incomplete
    _station: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> WeatherStationInfoModel: ...
