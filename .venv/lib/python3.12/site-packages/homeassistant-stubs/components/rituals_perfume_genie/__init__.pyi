from .const import ACCOUNT_HASH as ACCOUNT_HASH, DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from pyrituals import Diffuser as Diffuser

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
@callback
def async_migrate_entities_unique_ids(hass: HomeAssistant, config_entry: ConfigEntry, diffusers: list[Diffuser]) -> None: ...
