from .coordinator import Enigma2UpdateCoordinator as Enigma2UpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

type Enigma2ConfigEntry = ConfigEntry[Enigma2UpdateCoordinator]
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Enigma2ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
