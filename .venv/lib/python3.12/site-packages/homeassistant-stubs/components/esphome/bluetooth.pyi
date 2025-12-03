from .entry_data import RuntimeEntryData as RuntimeEntryData
from aioesphomeapi import APIClient as APIClient, DeviceInfo as DeviceInfo
from homeassistant.components.bluetooth import async_register_scanner as async_register_scanner
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as hass_callback

@hass_callback
def _async_unload(unload_callbacks: list[CALLBACK_TYPE]) -> None: ...
@hass_callback
def async_connect_scanner(hass: HomeAssistant, entry_data: RuntimeEntryData, cli: APIClient, device_info: DeviceInfo) -> CALLBACK_TYPE: ...
