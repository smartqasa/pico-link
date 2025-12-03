from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ID as CONF_ID, CONF_LOCATION as CONF_LOCATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

CONFIG_SCHEMA: Incomplete
_LOGGER: Incomplete
TVCameraConfigEntry = ConfigEntry[TVDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TVCameraConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
