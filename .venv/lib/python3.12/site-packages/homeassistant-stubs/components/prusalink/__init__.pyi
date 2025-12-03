from .config_flow import ConfigFlow as ConfigFlow
from .const import DOMAIN as DOMAIN
from .coordinator import InfoUpdateCoordinator as InfoUpdateCoordinator, JobUpdateCoordinator as JobUpdateCoordinator, LegacyStatusCoordinator as LegacyStatusCoordinator, StatusCoordinator as StatusCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
