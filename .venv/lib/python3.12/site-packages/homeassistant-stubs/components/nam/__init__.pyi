from .const import ATTR_SDS011 as ATTR_SDS011, ATTR_SPS30 as ATTR_SPS30, DOMAIN as DOMAIN
from .coordinator import NAMDataUpdateCoordinator as NAMDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete
type NAMConfigEntry = ConfigEntry[NAMDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: NAMConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NAMConfigEntry) -> bool: ...
