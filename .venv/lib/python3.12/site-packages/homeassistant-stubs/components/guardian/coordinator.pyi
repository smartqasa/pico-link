import asyncio
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from aioguardian import Client as Client
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_UPDATE_INTERVAL: Incomplete
SIGNAL_REBOOT_REQUESTED: str

class GuardianDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: ConfigEntry
    _api_coro: Incomplete
    _api_lock: Incomplete
    _client: Incomplete
    signal_reboot_requested: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry, client: Client, api_name: str, api_coro: Callable[[], Coroutine[Any, Any, dict[str, Any]]], api_lock: asyncio.Lock, valve_controller_uid: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    last_update_success: bool
    async def async_initialize(self) -> None: ...
