from .coordinator import AirGradientCoordinator as AirGradientCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
type AirGradientConfigEntry = ConfigEntry[AirGradientCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirGradientConfigEntry) -> bool: ...
