from .coordinator import SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

PLATFORMS: list[Platform]
type SchlageConfigEntry = ConfigEntry[SchlageDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: SchlageConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SchlageConfigEntry) -> bool: ...
