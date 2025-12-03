from .coordinator import BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.snmp import async_get_snmp_engine as async_get_snmp_engine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: Incomplete
type BrotherConfigEntry = ConfigEntry[BrotherDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
