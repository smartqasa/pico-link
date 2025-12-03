from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_ble_device_from_address as async_ble_device_from_address
from homeassistant.components.bluetooth.active_update_processor import ActiveBluetoothProcessorCoordinator as ActiveBluetoothProcessorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant
from oralb_ble import SensorUpdate as SensorUpdate

PLATFORMS: list[Platform]
_LOGGER: Incomplete
type OralBConfigEntry = ConfigEntry[ActiveBluetoothProcessorCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: OralBConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OralBConfigEntry) -> bool: ...
