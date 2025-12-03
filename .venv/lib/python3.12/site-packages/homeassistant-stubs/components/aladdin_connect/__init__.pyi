from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant

DOMAIN: str

async def async_setup_entry(hass: HomeAssistant, _: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
