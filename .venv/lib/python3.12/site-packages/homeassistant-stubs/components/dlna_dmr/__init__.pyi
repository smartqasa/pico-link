from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...
