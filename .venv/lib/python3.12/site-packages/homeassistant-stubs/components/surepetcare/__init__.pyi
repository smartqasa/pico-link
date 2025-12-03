from .const import ATTR_FLAP_ID as ATTR_FLAP_ID, ATTR_LOCATION as ATTR_LOCATION, ATTR_LOCK_STATE as ATTR_LOCK_STATE, ATTR_PET_NAME as ATTR_PET_NAME, DOMAIN as DOMAIN, SERVICE_SET_LOCK_STATE as SERVICE_SET_LOCK_STATE, SERVICE_SET_PET_LOCATION as SERVICE_SET_PET_LOCATION
from .coordinator import SurePetcareDataCoordinator as SurePetcareDataCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
PLATFORMS: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
