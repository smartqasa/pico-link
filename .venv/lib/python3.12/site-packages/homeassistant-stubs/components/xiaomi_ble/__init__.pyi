from .const import CONF_DISCOVERED_EVENT_CLASSES as CONF_DISCOVERED_EVENT_CLASSES, CONF_SLEEPY_DEVICE as CONF_SLEEPY_DEVICE, DOMAIN as DOMAIN, XIAOMI_BLE_EVENT as XIAOMI_BLE_EVENT, XiaomiBleEvent as XiaomiBleEvent
from .coordinator import XiaomiActiveBluetoothProcessorCoordinator as XiaomiActiveBluetoothProcessorCoordinator
from .types import XiaomiBLEConfigEntry as XiaomiBLEConfigEntry
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_ble_device_from_address as async_ble_device_from_address
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceRegistry as DeviceRegistry
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from xiaomi_ble import SensorUpdate as SensorUpdate

PLATFORMS: list[Platform]
_LOGGER: Incomplete

def process_service_info(hass: HomeAssistant, entry: XiaomiBLEConfigEntry, device_registry: DeviceRegistry, service_info: BluetoothServiceInfoBleak) -> SensorUpdate: ...
def format_event_dispatcher_name(address: str, event_class: str) -> str: ...
def format_discovered_event_class(address: str) -> str: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: XiaomiBLEConfigEntry) -> bool: ...
