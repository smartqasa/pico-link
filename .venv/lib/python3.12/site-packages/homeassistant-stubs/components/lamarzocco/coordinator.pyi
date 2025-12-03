import abc
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pylamarzocco.clients.local import LaMarzoccoLocalClient as LaMarzoccoLocalClient
from pylamarzocco.devices.machine import LaMarzoccoMachine as LaMarzoccoMachine

SCAN_INTERVAL: Incomplete
FIRMWARE_UPDATE_INTERVAL: Incomplete
STATISTICS_UPDATE_INTERVAL: Incomplete
_LOGGER: Incomplete

@dataclass
class LaMarzoccoRuntimeData:
    config_coordinator: LaMarzoccoConfigUpdateCoordinator
    firmware_coordinator: LaMarzoccoFirmwareUpdateCoordinator
    statistics_coordinator: LaMarzoccoStatisticsUpdateCoordinator
type LaMarzoccoConfigEntry = ConfigEntry[LaMarzoccoRuntimeData]

class LaMarzoccoUpdateCoordinator(DataUpdateCoordinator[None], metaclass=abc.ABCMeta):
    _default_update_interval = SCAN_INTERVAL
    config_entry: LaMarzoccoConfigEntry
    device: Incomplete
    local_connection_configured: Incomplete
    _local_client: Incomplete
    new_device_callback: list[Callable]
    def __init__(self, hass: HomeAssistant, entry: LaMarzoccoConfigEntry, device: LaMarzoccoMachine, local_client: LaMarzoccoLocalClient | None = None) -> None: ...
    async def _async_update_data(self) -> None: ...
    @abstractmethod
    async def _internal_async_update_data(self) -> None: ...

class LaMarzoccoConfigUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    _scale_address: str | None
    async def _async_connect_websocket(self) -> None: ...
    async def _internal_async_update_data(self) -> None: ...
    @callback
    def _async_add_remove_scale(self) -> None: ...

class LaMarzoccoFirmwareUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    _default_update_interval = FIRMWARE_UPDATE_INTERVAL
    async def _internal_async_update_data(self) -> None: ...

class LaMarzoccoStatisticsUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    _default_update_interval = STATISTICS_UPDATE_INTERVAL
    async def _internal_async_update_data(self) -> None: ...
