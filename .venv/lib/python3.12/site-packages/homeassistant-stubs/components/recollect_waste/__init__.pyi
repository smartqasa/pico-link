from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiorecollect.client import PickupEvent as PickupEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

DEFAULT_NAME: str
DEFAULT_UPDATE_INTERVAL: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
