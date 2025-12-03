from .const import CONF_EXPIRATION as CONF_EXPIRATION
from .coordinator import FytaCoordinator as FytaCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.util.dt import async_get_time_zone as async_get_time_zone

_LOGGER: Incomplete
PLATFORMS: Incomplete
type FytaConfigEntry = ConfigEntry[FytaCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: FytaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FytaConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: FytaConfigEntry) -> bool: ...
