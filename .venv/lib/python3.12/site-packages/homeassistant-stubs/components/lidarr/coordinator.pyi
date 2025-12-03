import abc
from .const import DEFAULT_MAX_RECORDS as DEFAULT_MAX_RECORDS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from aiopyarr import LidarrAlbum, LidarrQueue, LidarrRootFolder
from aiopyarr.lidarr_client import LidarrClient as LidarrClient
from aiopyarr.models.host_configuration import PyArrHostConfiguration as PyArrHostConfiguration
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Generic, TypeVar

T = TypeVar('T', bound=list[LidarrRootFolder] | LidarrQueue | str | LidarrAlbum | int)

class LidarrDataUpdateCoordinator(DataUpdateCoordinator[T], ABC, Generic[T], metaclass=abc.ABCMeta):
    config_entry: ConfigEntry
    api_client: Incomplete
    host_configuration: Incomplete
    def __init__(self, hass: HomeAssistant, host_configuration: PyArrHostConfiguration, api_client: LidarrClient) -> None: ...
    async def _async_update_data(self) -> T: ...
    @abstractmethod
    async def _fetch_data(self) -> T: ...

class DiskSpaceDataUpdateCoordinator(LidarrDataUpdateCoordinator[list[LidarrRootFolder]]):
    async def _fetch_data(self) -> list[LidarrRootFolder]: ...

class QueueDataUpdateCoordinator(LidarrDataUpdateCoordinator[LidarrQueue]):
    async def _fetch_data(self) -> LidarrQueue: ...

class StatusDataUpdateCoordinator(LidarrDataUpdateCoordinator[str]):
    async def _fetch_data(self) -> str: ...

class WantedDataUpdateCoordinator(LidarrDataUpdateCoordinator[LidarrAlbum]):
    async def _fetch_data(self) -> LidarrAlbum: ...

class AlbumsDataUpdateCoordinator(LidarrDataUpdateCoordinator[int]):
    async def _fetch_data(self) -> int: ...
