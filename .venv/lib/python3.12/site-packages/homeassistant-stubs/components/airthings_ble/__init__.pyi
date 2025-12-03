from .const import MAX_RETRIES_AFTER_STARTUP as MAX_RETRIES_AFTER_STARTUP
from .coordinator import AirthingsBLEConfigEntry as AirthingsBLEConfigEntry, AirthingsBLEDataUpdateCoordinator as AirthingsBLEDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AirthingsBLEConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirthingsBLEConfigEntry) -> bool: ...
