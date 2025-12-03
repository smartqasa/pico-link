from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarDataUpdateCoordinator as PeblarDataUpdateCoordinator, PeblarRuntimeData as PeblarRuntimeData, PeblarUserConfigurationDataUpdateCoordinator as PeblarUserConfigurationDataUpdateCoordinator, PeblarVersionDataUpdateCoordinator as PeblarVersionDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PeblarConfigEntry) -> bool: ...
