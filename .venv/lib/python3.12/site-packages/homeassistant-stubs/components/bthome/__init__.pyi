from .const import BTHOME_BLE_EVENT as BTHOME_BLE_EVENT, BTHomeBleEvent as BTHomeBleEvent, CONF_BINDKEY as CONF_BINDKEY, CONF_DISCOVERED_EVENT_CLASSES as CONF_DISCOVERED_EVENT_CLASSES, CONF_SLEEPY_DEVICE as CONF_SLEEPY_DEVICE, DOMAIN as DOMAIN
from .coordinator import BTHomePassiveBluetoothProcessorCoordinator as BTHomePassiveBluetoothProcessorCoordinator
from .types import BTHomeConfigEntry as BTHomeConfigEntry
from _typeshed import Incomplete
from bthome_ble import SensorUpdate as SensorUpdate
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceRegistry as DeviceRegistry
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.util.signal_type import SignalType as SignalType

PLATFORMS: list[Platform]
_LOGGER: Incomplete

def process_service_info(hass: HomeAssistant, entry: BTHomeConfigEntry, device_registry: DeviceRegistry, service_info: BluetoothServiceInfoBleak) -> SensorUpdate: ...
def format_event_dispatcher_name(address: str, event_class: str) -> SignalType[BTHomeBleEvent]: ...
def format_discovered_event_class(address: str) -> SignalType[str, BTHomeBleEvent]: ...
async def async_setup_entry(hass: HomeAssistant, entry: BTHomeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BTHomeConfigEntry) -> bool: ...
