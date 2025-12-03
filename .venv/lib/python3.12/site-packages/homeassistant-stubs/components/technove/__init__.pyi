from .coordinator import TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete
TechnoVEConfigEntry = ConfigEntry[TechnoVEDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TechnoVEConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
