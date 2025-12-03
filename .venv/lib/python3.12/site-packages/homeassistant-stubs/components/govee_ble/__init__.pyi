from .coordinator import GoveeBLEBluetoothProcessorCoordinator as GoveeBLEBluetoothProcessorCoordinator, GoveeBLEConfigEntry as GoveeBLEConfigEntry, process_service_info as process_service_info
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: GoveeBLEConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoveeBLEConfigEntry) -> bool: ...
