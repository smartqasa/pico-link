from .const import SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant import config_entries as config_entries
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import BaseDataUpdateCoordinatorProtocol as BaseDataUpdateCoordinatorProtocol, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from ring_doorbell import Ring as Ring, RingDevices, RingEvent as RingEvent
from typing import Any

_LOGGER: Incomplete

async def _call_api[*_Ts, _R](hass: HomeAssistant, target: Callable[[*_Ts], Coroutine[Any, Any, _R]], *args: *_Ts, msg_suffix: str = '') -> _R: ...

class RingDataCoordinator(DataUpdateCoordinator[RingDevices]):
    ring_api: Ring
    first_call: bool
    def __init__(self, hass: HomeAssistant, ring_api: Ring) -> None: ...
    async def _async_update_data(self) -> RingDevices: ...

class RingListenCoordinator(BaseDataUpdateCoordinatorProtocol):
    config_entry: config_entries.ConfigEntry
    hass: Incomplete
    logger: Incomplete
    ring_api: Ring
    event_listener: Incomplete
    _listeners: dict[CALLBACK_TYPE, tuple[CALLBACK_TYPE, object | None]]
    _listen_callback_id: int | None
    start_timeout: int
    def __init__(self, hass: HomeAssistant, ring_api: Ring, listen_credentials: dict[str, Any] | None, listen_credentials_updater: Callable[[dict[str, Any]], None]) -> None: ...
    alerts: Incomplete
    def index_alerts(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    async def _async_stop_listen(self) -> None: ...
    async def _async_start_listen(self) -> None: ...
    def _on_event(self, event: RingEvent) -> None: ...
    @callback
    def _async_update_listeners(self, doorbot_id: int | None = None) -> None: ...
    @callback
    def async_add_listener(self, update_callback: CALLBACK_TYPE, context: Any = None) -> Callable[[], None]: ...
