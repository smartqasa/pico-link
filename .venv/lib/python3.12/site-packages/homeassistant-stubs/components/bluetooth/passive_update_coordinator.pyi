import logging
from . import BluetoothChange as BluetoothChange, BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .update_coordinator import BasePassiveBluetoothCoordinator as BasePassiveBluetoothCoordinator
from collections.abc import Callable as Callable, Generator
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import BaseCoordinatorEntity as BaseCoordinatorEntity, BaseDataUpdateCoordinatorProtocol as BaseDataUpdateCoordinatorProtocol
from typing import Any
from typing_extensions import TypeVar

_PassiveBluetoothDataUpdateCoordinatorT = TypeVar('_PassiveBluetoothDataUpdateCoordinatorT', bound='PassiveBluetoothDataUpdateCoordinator', default='PassiveBluetoothDataUpdateCoordinator')

class PassiveBluetoothDataUpdateCoordinator(BasePassiveBluetoothCoordinator, BaseDataUpdateCoordinatorProtocol):
    _listeners: dict[CALLBACK_TYPE, tuple[CALLBACK_TYPE, object | None]]
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, address: str, mode: BluetoothScanningMode, connectable: bool = False) -> None: ...
    @property
    def available(self) -> bool: ...
    @callback
    def async_update_listeners(self) -> None: ...
    @callback
    def _async_handle_unavailable(self, service_info: BluetoothServiceInfoBleak) -> None: ...
    @callback
    def async_add_listener(self, update_callback: CALLBACK_TYPE, context: Any = None) -> Callable[[], None]: ...
    def async_contexts(self) -> Generator[Any]: ...
    _available: bool
    @callback
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...

class PassiveBluetoothCoordinatorEntity(BaseCoordinatorEntity[_PassiveBluetoothDataUpdateCoordinatorT]):
    async def async_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
