from .const import CONNECTION_EXCEPTIONS as CONNECTION_EXCEPTIONS, DOMAIN as DOMAIN
from .types import OncueConfigEntry as OncueConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

PLATFORMS: list[str]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OncueConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OncueConfigEntry) -> bool: ...
