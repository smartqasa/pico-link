from .const import DOMAIN as DOMAIN
from .coordinator import FAADataUpdateCoordinator as FAADataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
