from .const import CONF_USE_NEAREST as CONF_USE_NEAREST, DOMAIN as DOMAIN, MIN_UPDATE_INTERVAL as MIN_UPDATE_INTERVAL
from .coordinator import AirlyDataUpdateCoordinator as AirlyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete
_LOGGER: Incomplete
type AirlyConfigEntry = ConfigEntry[AirlyDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AirlyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirlyConfigEntry) -> bool: ...
