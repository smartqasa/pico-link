from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from govee_ble import GoveeBluetoothDeviceData as GoveeBluetoothDeviceData, ModelInfo as ModelInfo, SensorUpdate
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from logging import Logger

type GoveeBLEConfigEntry = ConfigEntry[GoveeBLEBluetoothProcessorCoordinator]
def process_service_info(hass: HomeAssistant, entry: GoveeBLEConfigEntry, service_info: BluetoothServiceInfoBleak) -> SensorUpdate: ...
def format_event_dispatcher_name(address: str, key: str) -> str: ...

class GoveeBLEBluetoothProcessorCoordinator(PassiveBluetoothProcessorCoordinator[SensorUpdate]):
    device_data: Incomplete
    entry: Incomplete
    model_info: ModelInfo | None
    def __init__(self, hass: HomeAssistant, logger: Logger, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], SensorUpdate], device_data: GoveeBluetoothDeviceData, entry: ConfigEntry) -> None: ...
    def set_model_info(self, device_type: str) -> None: ...

class GoveeBLEPassiveBluetoothDataProcessor[_T](PassiveBluetoothDataProcessor[_T, SensorUpdate]):
    coordinator: GoveeBLEBluetoothProcessorCoordinator
