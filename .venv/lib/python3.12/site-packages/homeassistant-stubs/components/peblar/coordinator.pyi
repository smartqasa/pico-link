from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from peblar import Peblar as Peblar, PeblarApi as PeblarApi, PeblarEVInterface as PeblarEVInterface, PeblarMeter as PeblarMeter, PeblarSystem as PeblarSystem, PeblarSystemInformation as PeblarSystemInformation, PeblarUserConfiguration, PeblarVersions as PeblarVersions
from typing import Any, Concatenate

@dataclass(kw_only=True)
class PeblarRuntimeData:
    data_coordinator: PeblarDataUpdateCoordinator
    system_information: PeblarSystemInformation
    user_configuration_coordinator: PeblarUserConfigurationDataUpdateCoordinator
    version_coordinator: PeblarVersionDataUpdateCoordinator
type PeblarConfigEntry = ConfigEntry[PeblarRuntimeData]

@dataclass(kw_only=True, frozen=True)
class PeblarVersionInformation:
    current: PeblarVersions
    available: PeblarVersions

@dataclass(kw_only=True)
class PeblarData:
    ev: PeblarEVInterface
    meter: PeblarMeter
    system: PeblarSystem

def _coordinator_exception_handler[_DataUpdateCoordinatorT: PeblarDataUpdateCoordinator | PeblarVersionDataUpdateCoordinator | PeblarUserConfigurationDataUpdateCoordinator, **_P](func: Callable[Concatenate[_DataUpdateCoordinatorT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_DataUpdateCoordinatorT, _P], Coroutine[Any, Any, Any]]: ...

class PeblarVersionDataUpdateCoordinator(DataUpdateCoordinator[PeblarVersionInformation]):
    peblar: Incomplete
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, peblar: Peblar) -> None: ...
    @_coordinator_exception_handler
    async def _async_update_data(self) -> PeblarVersionInformation: ...

class PeblarDataUpdateCoordinator(DataUpdateCoordinator[PeblarData]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, api: PeblarApi) -> None: ...
    @_coordinator_exception_handler
    async def _async_update_data(self) -> PeblarData: ...

class PeblarUserConfigurationDataUpdateCoordinator(DataUpdateCoordinator[PeblarUserConfiguration]):
    peblar: Incomplete
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, peblar: Peblar) -> None: ...
    @_coordinator_exception_handler
    async def _async_update_data(self) -> PeblarUserConfiguration: ...
