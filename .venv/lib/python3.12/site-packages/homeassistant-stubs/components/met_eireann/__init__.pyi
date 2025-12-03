import meteireann
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from types import MappingProxyType
from typing import Any, Self

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class MetEireannWeatherData:
    _config: Incomplete
    _weather_data: Incomplete
    current_weather_data: dict[str, Any]
    daily_forecast: list[dict[str, Any]]
    hourly_forecast: list[dict[str, Any]]
    def __init__(self, config: MappingProxyType[str, Any], weather_data: meteireann.WeatherData) -> None: ...
    async def fetch_data(self) -> Self: ...
