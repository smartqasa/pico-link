from .api import ApiAuthImpl as ApiAuthImpl, get_feature_access as get_feature_access
from .const import DATA_SERVICE as DATA_SERVICE, DATA_STORE as DATA_STORE, DOMAIN as DOMAIN, EVENT_DESCRIPTION as EVENT_DESCRIPTION, EVENT_END_DATE as EVENT_END_DATE, EVENT_END_DATETIME as EVENT_END_DATETIME, EVENT_IN as EVENT_IN, EVENT_IN_DAYS as EVENT_IN_DAYS, EVENT_IN_WEEKS as EVENT_IN_WEEKS, EVENT_LOCATION as EVENT_LOCATION, EVENT_START_DATE as EVENT_START_DATE, EVENT_START_DATETIME as EVENT_START_DATETIME, EVENT_SUMMARY as EVENT_SUMMARY, EVENT_TYPES_CONF as EVENT_TYPES_CONF, FeatureAccess as FeatureAccess
from .store import LocalCalendarStore as LocalCalendarStore
from _typeshed import Incomplete
from collections.abc import Mapping
from gcal_sync.api import GoogleCalendarService
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
from typing import Any

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
CONF_TRACK_NEW: str
CONF_CAL_ID: str
CONF_TRACK: str
CONF_SEARCH: str
CONF_IGNORE_AVAILABILITY: str
CONF_MAX_RESULTS: str
DEFAULT_CONF_OFFSET: str
EVENT_CALENDAR_ID: str
SERVICE_ADD_EVENT: str
YAML_DEVICES: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
_SINGLE_CALSEARCH_CONFIG: Incomplete
DEVICE_SCHEMA: Incomplete
_EVENT_IN_TYPES: Incomplete
ADD_EVENT_SERVICE_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def async_entry_has_scopes(entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_add_event_service(hass: HomeAssistant, calendar_service: GoogleCalendarService) -> None: ...
def get_calendar_info(hass: HomeAssistant, calendar: Mapping[str, Any]) -> dict[str, Any]: ...
def load_config(path: str) -> dict[str, Any]: ...
def update_config(path: str, calendar: dict[str, Any]) -> None: ...
