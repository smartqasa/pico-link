from .coordinator import TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete
type TautulliConfigEntry = ConfigEntry[TautulliDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TautulliConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TautulliConfigEntry) -> bool: ...
