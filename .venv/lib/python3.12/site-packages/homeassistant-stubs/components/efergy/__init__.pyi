from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from pyefergy import Efergy

PLATFORMS: Incomplete
type EfergyConfigEntry = ConfigEntry[Efergy]

async def async_setup_entry(hass: HomeAssistant, entry: EfergyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EfergyConfigEntry) -> bool: ...
