from .const import PLATFORMS as PLATFORMS
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

TVWeatherConfigEntry = ConfigEntry[TVDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TVWeatherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
