import dataclasses
from .models import USBDevice
from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.components import websocket_api
from homeassistant.core import CALLBACK_TYPE, Event, HomeAssistant, callback as hass_callback
from homeassistant.data_entry_flow import BaseServiceInfo
from homeassistant.helpers.debounce import Debouncer
from homeassistant.loader import USBMatcher
from pyudev import Device, MonitorObserver
from serial.tools.list_ports_common import ListPortInfo
from typing import Any

__all__ = ['async_is_plugged_in', 'async_register_scan_request_callback', 'USBCallbackMatcher', 'UsbServiceInfo']

class USBCallbackMatcher(USBMatcher): ...

@hass_callback
def async_register_scan_request_callback(hass: HomeAssistant, callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
@hass_callback
def async_is_plugged_in(hass: HomeAssistant, matcher: USBCallbackMatcher) -> bool: ...

@dataclasses.dataclass(slots=True)
class UsbServiceInfo(BaseServiceInfo):
    device: str
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None

class USBDiscovery:
    hass: Incomplete
    usb: Incomplete
    seen: set[tuple[str, ...]]
    observer_active: bool
    _request_debouncer: Debouncer[Coroutine[Any, Any, None]] | None
    _request_callbacks: list[CALLBACK_TYPE]
    initial_scan_done: bool
    _initial_scan_callbacks: list[CALLBACK_TYPE]
    def __init__(self, hass: HomeAssistant, usb: list[USBMatcher]) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_start(self, event: Event) -> None: ...
    @hass_callback
    def async_stop(self, event: Event) -> None: ...
    async def _async_start_monitor(self) -> None: ...
    def _get_monitor_observer(self) -> MonitorObserver | None: ...
    def _device_discovered(self, device: Device) -> None: ...
    @hass_callback
    def async_register_scan_request_callback(self, _callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    @hass_callback
    def async_register_initial_scan_callback(self, callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    async def _async_process_discovered_usb_device(self, device: USBDevice) -> None: ...
    async def _async_process_ports(self, ports: list[ListPortInfo]) -> None: ...
    async def _async_scan_serial(self) -> None: ...
    async def _async_scan(self) -> None: ...
    async def async_request_scan(self) -> None: ...
