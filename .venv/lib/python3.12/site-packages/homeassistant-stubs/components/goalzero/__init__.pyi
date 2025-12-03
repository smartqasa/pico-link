from .coordinator import GoalZeroConfigEntry as GoalZeroConfigEntry, GoalZeroDataUpdateCoordinator as GoalZeroDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: GoalZeroConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoalZeroConfigEntry) -> bool: ...
