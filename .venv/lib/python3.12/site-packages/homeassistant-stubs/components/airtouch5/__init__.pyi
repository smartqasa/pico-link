from airtouch5py.airtouch5_simple_client import Airtouch5SimpleClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
type Airtouch5ConfigEntry = ConfigEntry[Airtouch5SimpleClient]

async def async_setup_entry(hass: HomeAssistant, entry: Airtouch5ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: Airtouch5ConfigEntry) -> bool: ...
