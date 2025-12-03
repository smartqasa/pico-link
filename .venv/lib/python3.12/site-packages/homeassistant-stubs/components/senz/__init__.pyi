from .api import SENZConfigEntryAuth as SENZConfigEntryAuth
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiosenz import Thermostat
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow, httpx_client as httpx_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

UPDATE_INTERVAL: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
type SENZDataUpdateCoordinator = DataUpdateCoordinator[dict[str, Thermostat]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
