from .const import CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, CONF_USER_UUID as CONF_USER_UUID, DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_BATTERY as SENSOR_BATTERY, SENSOR_DOOR as SENSOR_DOOR, SENSOR_GARAGE_DOOR as SENSOR_GARAGE_DOOR, SENSOR_LEAK as SENSOR_LEAK, SENSOR_MISSING as SENSOR_MISSING, SENSOR_SAFE as SENSOR_SAFE, SENSOR_SLIDING as SENSOR_SLIDING, SENSOR_SMOKE_CO as SENSOR_SMOKE_CO, SENSOR_TEMPERATURE as SENSOR_TEMPERATURE, SENSOR_WINDOW_HINGED as SENSOR_WINDOW_HINGED
from .coordinator import NotionDataUpdateCoordinator as NotionDataUpdateCoordinator
from .util import async_get_client_with_credentials as async_get_client_with_credentials, async_get_client_with_refresh_token as async_get_client_with_refresh_token
from _typeshed import Incomplete
from aionotion.listener.models import ListenerKind
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: Incomplete
ATTR_SYSTEM_MODE: str
ATTR_SYSTEM_NAME: str
DEFAULT_SCAN_INTERVAL: Incomplete
TASK_TYPE_TO_LISTENER_MAP: dict[str, ListenerKind]

@callback
def is_uuid(value: str) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
