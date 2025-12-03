from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytradfri.command import Command as Command
from pytradfri.device import Device
from typing import Any

SCAN_INTERVAL: int

class TradfriDeviceDataUpdateCoordinator(DataUpdateCoordinator[Device]):
    api: Incomplete
    device: Incomplete
    _exception: Exception | None
    def __init__(self, hass: HomeAssistant, *, api: Callable[[Command | list[Command]], Any], device: Device) -> None: ...
    last_update_success: bool
    async def set_hub_available(self, available: bool) -> None: ...
    @callback
    def _observe_update(self, device: Device) -> None: ...
    @callback
    def _exception_callback(self, exc: Exception) -> None: ...
    update_interval: Incomplete
    async def _handle_exception(self, exc: Exception) -> None: ...
    async def _async_update_data(self) -> Device: ...
