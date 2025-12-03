import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from typing import Any

def handle_error(func: Callable[[Command | list[Command]], Any]) -> Callable[[Command | list[Command]], Coroutine[Any, Any, None]]: ...

class TradfriBaseEntity(CoordinatorEntity[TradfriDeviceDataUpdateCoordinator], metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _gateway_id: Incomplete
    _device: Device
    _device_id: Incomplete
    _api: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, gateway_id: str, api: Callable[[Command | list[Command]], Any]) -> None: ...
    @abstractmethod
    @callback
    def _refresh(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
