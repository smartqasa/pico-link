from .coordinator import JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

type JVCConfigEntry = ConfigEntry[JvcProjectorDataUpdateCoordinator]
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: JVCConfigEntry) -> bool: ...
