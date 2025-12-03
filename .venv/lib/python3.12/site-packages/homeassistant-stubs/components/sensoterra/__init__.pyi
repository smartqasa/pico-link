from .coordinator import SensoterraCoordinator as SensoterraCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
type SensoterraConfigEntry = ConfigEntry[SensoterraCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: SensoterraConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SensoterraConfigEntry) -> bool: ...
