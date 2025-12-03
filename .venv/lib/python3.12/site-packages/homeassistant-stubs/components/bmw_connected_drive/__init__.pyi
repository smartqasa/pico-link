from .const import ATTR_VIN as ATTR_VIN, CONF_READ_ONLY as CONF_READ_ONLY, DOMAIN as DOMAIN
from .coordinator import BMWConfigEntry as BMWConfigEntry, BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery as discovery

_LOGGER: Incomplete
SERVICE_SCHEMA: Incomplete
DEFAULT_OPTIONS: Incomplete
PLATFORMS: Incomplete
SERVICE_UPDATE_STATE: str

@callback
def _async_migrate_options_from_data_if_missing(hass: HomeAssistant, entry: BMWConfigEntry) -> None: ...
async def _async_migrate_entries(hass: HomeAssistant, config_entry: BMWConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: BMWConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BMWConfigEntry) -> bool: ...
