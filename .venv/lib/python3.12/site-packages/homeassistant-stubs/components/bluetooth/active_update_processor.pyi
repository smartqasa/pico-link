import logging
from . import BluetoothChange as BluetoothChange, BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .passive_update_processor import PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.debounce import Debouncer as Debouncer
from typing import Any

POLL_DEFAULT_COOLDOWN: int
POLL_DEFAULT_IMMEDIATE: bool

class ActiveBluetoothProcessorCoordinator[_DataT](PassiveBluetoothProcessorCoordinator[_DataT]):
    _needs_poll_method: Incomplete
    _poll_method: Incomplete
    _last_poll: float | None
    last_poll_successful: bool
    _last_service_info: BluetoothServiceInfoBleak | None
    _debounced_poll: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, *, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], _DataT], needs_poll_method: Callable[[BluetoothServiceInfoBleak, float | None], bool], poll_method: Callable[[BluetoothServiceInfoBleak], Coroutine[Any, Any, _DataT]] | None = None, poll_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = None, connectable: bool = True) -> None: ...
    def needs_poll(self, service_info: BluetoothServiceInfoBleak) -> bool: ...
    async def _async_poll_data(self, last_service_info: BluetoothServiceInfoBleak) -> _DataT: ...
    async def _async_poll(self) -> None: ...
    @callback
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...
    @callback
    def _async_stop(self) -> None: ...
