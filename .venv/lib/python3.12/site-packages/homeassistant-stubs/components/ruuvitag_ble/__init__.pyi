from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
