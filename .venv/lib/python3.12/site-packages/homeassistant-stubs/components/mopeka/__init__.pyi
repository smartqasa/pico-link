from .const import CONF_MEDIUM_TYPE as CONF_MEDIUM_TYPE, DEFAULT_MEDIUM_TYPE as DEFAULT_MEDIUM_TYPE
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
_LOGGER: Incomplete
type MopekaConfigEntry = ConfigEntry[PassiveBluetoothProcessorCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: MopekaConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: MopekaConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: MopekaConfigEntry) -> bool: ...
