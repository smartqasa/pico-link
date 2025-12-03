from .data import HistoryStats as HistoryStats, HistoryStatsState as HistoryStatsState
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.start import async_at_start as async_at_start
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete

class HistoryStatsUpdateCoordinator(DataUpdateCoordinator[HistoryStatsState]):
    _history_stats: Incomplete
    _subscriber_count: int
    _at_start_listener: CALLBACK_TYPE | None
    _track_events_listener: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant, history_stats: HistoryStats, config_entry: ConfigEntry | None, name: str) -> None: ...
    @callback
    def async_setup_state_listener(self) -> CALLBACK_TYPE: ...
    @callback
    def _async_remove_listener(self) -> None: ...
    @callback
    def _async_add_listener(self) -> None: ...
    @callback
    def _async_add_events_listener(self, *_: Any) -> None: ...
    async def _async_update_from_event(self, event: Event[EventStateChangedData]) -> None: ...
    async def _async_update_data(self) -> HistoryStatsState: ...
