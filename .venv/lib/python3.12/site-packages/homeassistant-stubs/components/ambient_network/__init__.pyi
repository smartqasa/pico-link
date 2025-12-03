from .coordinator import AmbientNetworkDataUpdateCoordinator as AmbientNetworkDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

type AmbientNetworkConfigEntry = ConfigEntry[AmbientNetworkDataUpdateCoordinator]
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AmbientNetworkConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AmbientNetworkConfigEntry) -> bool: ...
