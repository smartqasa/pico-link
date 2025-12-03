from . import api as api
from .const import ACCOUNT_COORDINATOR as ACCOUNT_COORDINATOR, DOMAIN as DOMAIN, HOP_COORDINATOR as HOP_COORDINATOR
from .coordinator import ElectricKiwiAccountDataCoordinator as ElectricKiwiAccountDataCoordinator, ElectricKiwiHOPDataCoordinator as ElectricKiwiHOPDataCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
