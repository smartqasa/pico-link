import transmission_rpc
from .const import ATTR_DELETE_DATA as ATTR_DELETE_DATA, ATTR_DOWNLOAD_PATH as ATTR_DOWNLOAD_PATH, ATTR_TORRENT as ATTR_TORRENT, CONF_ENTRY_ID as CONF_ENTRY_ID, DEFAULT_DELETE_DATA as DEFAULT_DELETE_DATA, DEFAULT_PATH as DEFAULT_PATH, DEFAULT_SSL as DEFAULT_SSL, DOMAIN as DOMAIN, SERVICE_ADD_TORRENT as SERVICE_ADD_TORRENT, SERVICE_REMOVE_TORRENT as SERVICE_REMOVE_TORRENT, SERVICE_START_TORRENT as SERVICE_START_TORRENT, SERVICE_STOP_TORRENT as SERVICE_STOP_TORRENT
from .coordinator import TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from .errors import AuthenticationError as AuthenticationError, CannotConnect as CannotConnect, UnknownError as UnknownError
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PATH as CONF_PATH, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import selector as selector
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
PLATFORMS: Incomplete
MIGRATION_NAME_TO_KEY: Incomplete
SERVICE_BASE_SCHEMA: Incomplete
SERVICE_ADD_TORRENT_SCHEMA: Incomplete
SERVICE_REMOVE_TORRENT_SCHEMA: Incomplete
SERVICE_START_TORRENT_SCHEMA: Incomplete
SERVICE_STOP_TORRENT_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
type TransmissionConfigEntry = ConfigEntry[TransmissionDataUpdateCoordinator]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
def _get_coordinator_from_service_data(hass: HomeAssistant, entry_id: str) -> TransmissionDataUpdateCoordinator: ...
def setup_hass_services(hass: HomeAssistant) -> None: ...
async def get_api(hass: HomeAssistant, entry: dict[str, Any]) -> transmission_rpc.Client: ...
