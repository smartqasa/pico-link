from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: list[Platform]
_LOGGER: Incomplete
type AirzoneConfigEntry = ConfigEntry[AirzoneUpdateCoordinator]

async def _async_migrate_unique_ids(hass: HomeAssistant, entry: AirzoneConfigEntry, coordinator: AirzoneUpdateCoordinator) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirzoneConfigEntry) -> bool: ...
