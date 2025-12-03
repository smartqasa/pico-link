import dataclasses
from . import CONF_IGNORE_AVAILABILITY as CONF_IGNORE_AVAILABILITY, CONF_SEARCH as CONF_SEARCH, CONF_TRACK as CONF_TRACK, DEFAULT_CONF_OFFSET as DEFAULT_CONF_OFFSET, DOMAIN as DOMAIN, YAML_DEVICES as YAML_DEVICES, get_calendar_info as get_calendar_info, load_config as load_config, update_config as update_config
from .api import get_feature_access as get_feature_access
from .const import DATA_SERVICE as DATA_SERVICE, DATA_STORE as DATA_STORE, EVENT_END_DATE as EVENT_END_DATE, EVENT_END_DATETIME as EVENT_END_DATETIME, EVENT_IN as EVENT_IN, EVENT_IN_DAYS as EVENT_IN_DAYS, EVENT_IN_WEEKS as EVENT_IN_WEEKS, EVENT_START_DATE as EVENT_START_DATE, EVENT_START_DATETIME as EVENT_START_DATETIME, FeatureAccess as FeatureAccess
from .coordinator import CalendarQueryUpdateCoordinator as CalendarQueryUpdateCoordinator, CalendarSyncUpdateCoordinator as CalendarSyncUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from datetime import datetime, timedelta
from gcal_sync.model import Calendar as Calendar, Event
from homeassistant.components.calendar import CREATE_EVENT_SCHEMA as CREATE_EVENT_SCHEMA, CalendarEntity as CalendarEntity, CalendarEntityDescription as CalendarEntityDescription, CalendarEntityFeature as CalendarEntityFeature, CalendarEvent as CalendarEvent, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, EVENT_DESCRIPTION as EVENT_DESCRIPTION, EVENT_END as EVENT_END, EVENT_LOCATION as EVENT_LOCATION, EVENT_RRULE as EVENT_RRULE, EVENT_START as EVENT_START, EVENT_SUMMARY as EVENT_SUMMARY, extract_offset as extract_offset, is_offset_reached as is_offset_reached
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, PlatformNotReady as PlatformNotReady
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
SYNC_EVENT_MIN_TIME: Incomplete
OPAQUE: str
RRULE_PREFIX: str
SERVICE_CREATE_EVENT: str

@dataclasses.dataclass(frozen=True, kw_only=True)
class GoogleCalendarEntityDescription(CalendarEntityDescription):
    name: str | None
    entity_id: str | None
    read_only: bool
    ignore_availability: bool
    offset: str | None
    search: str | None
    local_sync: bool
    device_id: str
    working_location: bool = ...

def _get_entity_descriptions(hass: HomeAssistant, config_entry: ConfigEntry, calendar_item: Calendar, calendar_info: Mapping[str, Any]) -> list[GoogleCalendarEntityDescription]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GoogleCalendarEntity(CoordinatorEntity[CalendarSyncUpdateCoordinator | CalendarQueryUpdateCoordinator], CalendarEntity):
    entity_description: GoogleCalendarEntityDescription
    _attr_has_entity_name: bool
    calendar_id: Incomplete
    _ignore_availability: Incomplete
    _offset: Incomplete
    _event: CalendarEvent | None
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, coordinator: CalendarSyncUpdateCoordinator | CalendarQueryUpdateCoordinator, calendar_id: str, entity_description: GoogleCalendarEntityDescription, unique_id: str | None) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
    @property
    def offset_reached(self) -> bool: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    def _event_filter(self, event: Event) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _event_with_offset(self) -> tuple[CalendarEvent | None, timedelta | None]: ...
    async def async_create_event(self, **kwargs: Any) -> None: ...
    async def async_delete_event(self, uid: str, recurrence_id: str | None = None, recurrence_range: str | None = None) -> None: ...

def _get_calendar_event(event: Event) -> CalendarEvent: ...
async def async_create_event(entity: GoogleCalendarEntity, call: ServiceCall) -> None: ...
