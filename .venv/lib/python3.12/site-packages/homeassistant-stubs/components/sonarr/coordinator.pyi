from .const import CONF_UPCOMING_DAYS as CONF_UPCOMING_DAYS, CONF_WANTED_MAX_ITEMS as CONF_WANTED_MAX_ITEMS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiopyarr import Command, Diskspace, SonarrCalendar, SonarrQueue, SonarrSeries, SonarrWantedMissing, SystemStatus
from aiopyarr.models.host_configuration import PyArrHostConfiguration as PyArrHostConfiguration
from aiopyarr.sonarr_client import SonarrClient as SonarrClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import TypeVar

SonarrDataT = TypeVar('SonarrDataT', bound=list[SonarrCalendar] | list[Command] | list[Diskspace] | SonarrQueue | list[SonarrSeries] | SystemStatus | SonarrWantedMissing)

class SonarrDataUpdateCoordinator(DataUpdateCoordinator[SonarrDataT]):
    config_entry: ConfigEntry
    api_client: Incomplete
    host_configuration: Incomplete
    system_version: str | None
    def __init__(self, hass: HomeAssistant, host_configuration: PyArrHostConfiguration, api_client: SonarrClient) -> None: ...
    async def _async_update_data(self) -> SonarrDataT: ...
    async def _fetch_data(self) -> SonarrDataT: ...

class CalendarDataUpdateCoordinator(SonarrDataUpdateCoordinator[list[SonarrCalendar]]):
    async def _fetch_data(self) -> list[SonarrCalendar]: ...

class CommandsDataUpdateCoordinator(SonarrDataUpdateCoordinator[list[Command]]):
    async def _fetch_data(self) -> list[Command]: ...

class DiskSpaceDataUpdateCoordinator(SonarrDataUpdateCoordinator[list[Diskspace]]):
    async def _fetch_data(self) -> list[Diskspace]: ...

class QueueDataUpdateCoordinator(SonarrDataUpdateCoordinator[SonarrQueue]):
    async def _fetch_data(self) -> SonarrQueue: ...

class SeriesDataUpdateCoordinator(SonarrDataUpdateCoordinator[list[SonarrSeries]]):
    async def _fetch_data(self) -> list[SonarrSeries]: ...

class StatusDataUpdateCoordinator(SonarrDataUpdateCoordinator[SystemStatus]):
    async def _fetch_data(self) -> SystemStatus: ...

class WantedDataUpdateCoordinator(SonarrDataUpdateCoordinator[SonarrWantedMissing]):
    async def _fetch_data(self) -> SonarrWantedMissing: ...
