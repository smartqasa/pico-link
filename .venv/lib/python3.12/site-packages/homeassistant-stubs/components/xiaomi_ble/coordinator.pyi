from .const import CONF_SLEEPY_DEVICE as CONF_SLEEPY_DEVICE
from .types import XiaomiBLEConfigEntry as XiaomiBLEConfigEntry
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth.active_update_processor import ActiveBluetoothProcessorCoordinator as ActiveBluetoothProcessorCoordinator
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from logging import Logger
from typing import Any
from xiaomi_ble import SensorUpdate, XiaomiBluetoothDeviceData as XiaomiBluetoothDeviceData

class XiaomiActiveBluetoothProcessorCoordinator(ActiveBluetoothProcessorCoordinator[SensorUpdate]):
    discovered_event_classes: Incomplete
    device_data: Incomplete
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], SensorUpdate], needs_poll_method: Callable[[BluetoothServiceInfoBleak, float | None], bool], device_data: XiaomiBluetoothDeviceData, discovered_event_classes: set[str], poll_method: Callable[[BluetoothServiceInfoBleak], Coroutine[Any, Any, SensorUpdate]] | None = None, poll_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = None, entry: XiaomiBLEConfigEntry, connectable: bool = True) -> None: ...
    @property
    def sleepy_device(self) -> bool: ...

class XiaomiPassiveBluetoothDataProcessor[_T](PassiveBluetoothDataProcessor[_T, SensorUpdate]):
    coordinator: XiaomiActiveBluetoothProcessorCoordinator
