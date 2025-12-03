from .coordinator import SpeedTestDataCoordinator as SpeedTestDataCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.start import async_at_started as async_at_started

PLATFORMS: Incomplete
type SpeedTestConfigEntry = ConfigEntry[SpeedTestDataCoordinator]

async def async_setup_entry(hass: HomeAssistant, config_entry: SpeedTestConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
