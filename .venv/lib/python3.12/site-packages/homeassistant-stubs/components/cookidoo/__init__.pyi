from .coordinator import CookidooConfigEntry as CookidooConfigEntry, CookidooDataUpdateCoordinator as CookidooDataUpdateCoordinator
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_EMAIL as CONF_EMAIL, CONF_LANGUAGE as CONF_LANGUAGE, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: CookidooConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CookidooConfigEntry) -> bool: ...
