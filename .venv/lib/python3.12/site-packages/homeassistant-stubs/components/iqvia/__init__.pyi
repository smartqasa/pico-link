from .const import CONF_ZIP_CODE as CONF_ZIP_CODE, DOMAIN as DOMAIN, LOGGER as LOGGER, TYPE_ALLERGY_FORECAST as TYPE_ALLERGY_FORECAST, TYPE_ALLERGY_INDEX as TYPE_ALLERGY_INDEX, TYPE_ALLERGY_OUTLOOK as TYPE_ALLERGY_OUTLOOK, TYPE_ASTHMA_FORECAST as TYPE_ASTHMA_FORECAST, TYPE_ASTHMA_INDEX as TYPE_ASTHMA_INDEX, TYPE_DISEASE_FORECAST as TYPE_DISEASE_FORECAST, TYPE_DISEASE_INDEX as TYPE_DISEASE_INDEX
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

DEFAULT_ATTRIBUTION: str
DEFAULT_SCAN_INTERVAL: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
