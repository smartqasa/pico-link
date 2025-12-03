import abc
from . import RadarrConfigEntry as RadarrConfigEntry
from .const import DEFAULT_MAX_RECORDS as DEFAULT_MAX_RECORDS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from aiopyarr import Health, RadarrCalendarItem as RadarrCalendarItem, RootFolder, SystemStatus
from aiopyarr.models.host_configuration import PyArrHostConfiguration as PyArrHostConfiguration
from aiopyarr.radarr_client import RadarrClient as RadarrClient
from dataclasses import dataclass
from datetime import date, datetime
from homeassistant.components.calendar import CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Generic, TypeVar

T = TypeVar('T', bound=SystemStatus | list[RootFolder] | list[Health] | int | None)

@dataclass
class RadarrEventMixIn:
    release_type: str

@dataclass
class RadarrEvent(CalendarEvent, RadarrEventMixIn): ...

class RadarrDataUpdateCoordinator(DataUpdateCoordinator[T], ABC, Generic[T], metaclass=abc.ABCMeta):
    config_entry: RadarrConfigEntry
    _update_interval: Incomplete
    api_client: Incomplete
    host_configuration: Incomplete
    def __init__(self, hass: HomeAssistant, host_configuration: PyArrHostConfiguration, api_client: RadarrClient) -> None: ...
    async def _async_update_data(self) -> T: ...
    @abstractmethod
    async def _fetch_data(self) -> T: ...

class StatusDataUpdateCoordinator(RadarrDataUpdateCoordinator[SystemStatus]):
    async def _fetch_data(self) -> SystemStatus: ...

class DiskSpaceDataUpdateCoordinator(RadarrDataUpdateCoordinator[list[RootFolder]]):
    async def _fetch_data(self) -> list[RootFolder]: ...

class HealthDataUpdateCoordinator(RadarrDataUpdateCoordinator[list[Health]]):
    async def _fetch_data(self) -> list[Health]: ...

class MoviesDataUpdateCoordinator(RadarrDataUpdateCoordinator[int]):
    async def _fetch_data(self) -> int: ...

class QueueDataUpdateCoordinator(RadarrDataUpdateCoordinator):
    async def _fetch_data(self) -> int: ...

class CalendarUpdateCoordinator(RadarrDataUpdateCoordinator[None]):
    _update_interval: Incomplete
    event: RadarrEvent | None
    _events: list[RadarrEvent]
    def __init__(self, hass: HomeAssistant, host_configuration: PyArrHostConfiguration, api_client: RadarrClient) -> None: ...
    async def _fetch_data(self) -> None: ...
    async def async_get_events(self, start_date: datetime, end_date: datetime) -> list[RadarrEvent]: ...
    async def _async_get_events(self, _date: date) -> None: ...

def _get_calendar_event(event: RadarrCalendarItem) -> RadarrEvent: ...
