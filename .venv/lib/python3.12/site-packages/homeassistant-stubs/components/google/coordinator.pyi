from _typeshed import Incomplete
from collections.abc import Iterable
from datetime import datetime
from gcal_sync.api import GoogleCalendarService as GoogleCalendarService
from gcal_sync.model import Event
from gcal_sync.sync import CalendarEventSyncManager as CalendarEventSyncManager
from gcal_sync.timeline import Timeline
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
MIN_TIME_BETWEEN_UPDATES: Incomplete
MAX_UPCOMING_EVENTS: int

def _truncate_timeline(timeline: Timeline, max_events: int) -> Timeline: ...

class CalendarSyncUpdateCoordinator(DataUpdateCoordinator[Timeline]):
    config_entry: ConfigEntry
    sync: Incomplete
    _upcoming_timeline: Timeline | None
    def __init__(self, hass: HomeAssistant, sync: CalendarEventSyncManager, name: str) -> None: ...
    async def _async_update_data(self) -> Timeline: ...
    async def async_get_events(self, start_date: datetime, end_date: datetime) -> Iterable[Event]: ...
    @property
    def upcoming(self) -> Iterable[Event] | None: ...

class CalendarQueryUpdateCoordinator(DataUpdateCoordinator[list[Event]]):
    config_entry: ConfigEntry
    calendar_service: Incomplete
    calendar_id: Incomplete
    _search: Incomplete
    def __init__(self, hass: HomeAssistant, calendar_service: GoogleCalendarService, name: str, calendar_id: str, search: str | None) -> None: ...
    async def async_get_events(self, start_date: datetime, end_date: datetime) -> Iterable[Event]: ...
    async def _async_update_data(self) -> list[Event]: ...
    @property
    def upcoming(self) -> Iterable[Event] | None: ...
