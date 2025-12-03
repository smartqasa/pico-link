from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL_DAILY_FORECAST as UPDATE_INTERVAL_DAILY_FORECAST, UPDATE_INTERVAL_OBSERVATION as UPDATE_INTERVAL_OBSERVATION
from .coordinator import AccuWeatherConfigEntry as AccuWeatherConfigEntry, AccuWeatherDailyForecastDataUpdateCoordinator as AccuWeatherDailyForecastDataUpdateCoordinator, AccuWeatherData as AccuWeatherData, AccuWeatherObservationDataUpdateCoordinator as AccuWeatherObservationDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry) -> bool: ...
