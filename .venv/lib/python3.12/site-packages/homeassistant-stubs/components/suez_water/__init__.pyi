from .coordinator import SuezWaterConfigEntry as SuezWaterConfigEntry, SuezWaterCoordinator as SuezWaterCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: SuezWaterConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SuezWaterConfigEntry) -> bool: ...
