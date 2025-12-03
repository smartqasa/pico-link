from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from .coordinator import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator, async_validate_input as async_validate_input
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
