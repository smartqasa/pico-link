from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.async_ import gather_with_limited_concurrency as gather_with_limited_concurrency
from pytile.tile import Tile as Tile

PLATFORMS: Incomplete
DEVICE_TYPES: Incomplete
DEFAULT_INIT_TASK_LIMIT: int
DEFAULT_UPDATE_INTERVAL: Incomplete
CONF_SHOW_INACTIVE: str

@dataclass
class TileData:
    coordinators: dict[str, DataUpdateCoordinator[None]]
    tiles: dict[str, Tile]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
