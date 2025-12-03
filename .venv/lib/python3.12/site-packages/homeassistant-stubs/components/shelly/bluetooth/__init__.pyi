from ..const import BLEScannerMode as BLEScannerMode
from ..coordinator import ShellyRpcCoordinator as ShellyRpcCoordinator
from homeassistant.components.bluetooth import async_register_scanner as async_register_scanner
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac

async def async_connect_scanner(hass: HomeAssistant, coordinator: ShellyRpcCoordinator, scanner_mode: BLEScannerMode) -> CALLBACK_TYPE: ...
