from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: list[Platform]
type AirzoneCloudConfigEntry = ConfigEntry[AirzoneUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneCloudConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirzoneCloudConfigEntry) -> bool: ...
