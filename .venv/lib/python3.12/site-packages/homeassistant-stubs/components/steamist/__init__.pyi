from .const import DISCOVERY as DISCOVERY, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN
from .coordinator import SteamistDataUpdateCoordinator as SteamistDataUpdateCoordinator
from .discovery import async_discover_device as async_discover_device, async_discover_devices as async_discover_devices, async_get_discovery as async_get_discovery, async_trigger_discovery as async_trigger_discovery, async_update_entry_from_discovery as async_update_entry_from_discovery
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[str]
DISCOVERY_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
