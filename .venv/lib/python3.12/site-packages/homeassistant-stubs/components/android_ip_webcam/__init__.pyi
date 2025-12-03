from .coordinator import AndroidIPCamConfigEntry as AndroidIPCamConfigEntry, AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AndroidIPCamConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AndroidIPCamConfigEntry) -> bool: ...
