from .const import API as API, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, COORDINATOR as COORDINATOR, DOMAIN as DOMAIN
from .coordinator import Tami4EdgeCoordinator as Tami4EdgeCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
