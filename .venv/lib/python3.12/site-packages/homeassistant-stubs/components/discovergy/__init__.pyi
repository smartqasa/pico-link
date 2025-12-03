from .coordinator import DiscovergyUpdateCoordinator as DiscovergyUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

PLATFORMS: Incomplete
type DiscovergyConfigEntry = ConfigEntry[list[DiscovergyUpdateCoordinator]]

async def async_setup_entry(hass: HomeAssistant, entry: DiscovergyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DiscovergyConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: DiscovergyConfigEntry) -> None: ...
