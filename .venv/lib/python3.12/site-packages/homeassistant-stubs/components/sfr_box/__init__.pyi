from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, PLATFORMS_WITH_AUTH as PLATFORMS_WITH_AUTH
from .coordinator import SFRDataUpdateCoordinator as SFRDataUpdateCoordinator
from .models import DomainData as DomainData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
