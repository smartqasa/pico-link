from .const import PLATFORMS as PLATFORMS
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

TVFerryConfigEntry = ConfigEntry[TVDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TVFerryConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
