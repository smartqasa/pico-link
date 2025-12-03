from .coordinator import PureEnergieDataUpdateCoordinator as PureEnergieDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
type PureEnergieConfigEntry = ConfigEntry[PureEnergieDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: PureEnergieConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PureEnergieConfigEntry) -> bool: ...
