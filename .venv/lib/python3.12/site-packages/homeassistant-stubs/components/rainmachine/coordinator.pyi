from . import RainMachineConfigEntry as RainMachineConfigEntry
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SIGNAL_REBOOT_COMPLETED: str
SIGNAL_REBOOT_REQUESTED: str

class RainMachineDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    config_entry: RainMachineConfigEntry
    _rebooting: bool
    _signal_handler_unsubs: list[Callable[[], None]]
    signal_reboot_completed: Incomplete
    signal_reboot_requested: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: RainMachineConfigEntry, name: str, api_category: str, update_interval: timedelta, update_method: Callable[[], Coroutine[Any, Any, dict]]) -> None: ...
    last_update_success: bool
    @callback
    def async_initialize(self) -> None: ...
