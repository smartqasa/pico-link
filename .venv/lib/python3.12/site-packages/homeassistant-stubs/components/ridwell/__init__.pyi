from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_TYPE_NEXT_PICKUP as SENSOR_TYPE_NEXT_PICKUP
from .coordinator import RidwellDataUpdateCoordinator as RidwellDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
