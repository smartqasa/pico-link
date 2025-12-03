from .const import PLATFORMS as PLATFORMS
from .coordinator import FileSizeCoordinator as FileSizeCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FILE_PATH as CONF_FILE_PATH
from homeassistant.core import HomeAssistant as HomeAssistant

type FileSizeConfigEntry = ConfigEntry[FileSizeCoordinator]
async def async_setup_entry(hass: HomeAssistant, entry: FileSizeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
