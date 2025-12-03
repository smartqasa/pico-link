from .coordinator import AwairCloudDataUpdateCoordinator as AwairCloudDataUpdateCoordinator, AwairConfigEntry as AwairConfigEntry, AwairDataUpdateCoordinator as AwairDataUpdateCoordinator, AwairLocalDataUpdateCoordinator as AwairLocalDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AwairConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: AwairConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: AwairConfigEntry) -> bool: ...
