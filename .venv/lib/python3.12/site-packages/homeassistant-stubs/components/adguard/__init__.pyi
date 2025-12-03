from .const import CONF_FORCE as CONF_FORCE, DOMAIN as DOMAIN, SERVICE_ADD_URL as SERVICE_ADD_URL, SERVICE_DISABLE_URL as SERVICE_DISABLE_URL, SERVICE_ENABLE_URL as SERVICE_ENABLE_URL, SERVICE_REFRESH as SERVICE_REFRESH, SERVICE_REMOVE_URL as SERVICE_REMOVE_URL
from _typeshed import Incomplete
from adguardhome import AdGuardHome
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

SERVICE_URL_SCHEMA: Incomplete
SERVICE_ADD_URL_SCHEMA: Incomplete
SERVICE_REFRESH_SCHEMA: Incomplete
PLATFORMS: Incomplete
type AdGuardConfigEntry = ConfigEntry[AdGuardData]

@dataclass
class AdGuardData:
    client: AdGuardHome
    version: str

async def async_setup_entry(hass: HomeAssistant, entry: AdGuardConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AdGuardConfigEntry) -> bool: ...
