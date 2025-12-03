from .const import CONF_DEVICE_API_ID as CONF_DEVICE_API_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from pyegps import PowerStripUSB as PowerStripUSB

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
