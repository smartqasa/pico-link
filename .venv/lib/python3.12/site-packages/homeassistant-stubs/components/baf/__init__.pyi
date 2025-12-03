from .const import QUERY_INTERVAL as QUERY_INTERVAL, RUN_TIMEOUT as RUN_TIMEOUT
from aiobafi6 import Device
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

type BAFConfigEntry = ConfigEntry[Device]
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: BAFConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BAFConfigEntry) -> bool: ...
