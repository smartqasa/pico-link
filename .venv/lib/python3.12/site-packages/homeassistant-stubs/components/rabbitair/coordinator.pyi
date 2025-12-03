from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from rabbitair import Client as Client, State
from typing import Any

_LOGGER: Incomplete

class RabbitAirDebouncer(Debouncer[Coroutine[Any, Any, None]]):
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_call(self) -> None: ...
    def has_pending_call(self) -> bool: ...

class RabbitAirDataUpdateCoordinator(DataUpdateCoordinator[State]):
    device: Incomplete
    def __init__(self, hass: HomeAssistant, device: Client) -> None: ...
    async def _async_update_data(self) -> State: ...
    async def _async_refresh(self, log_failures: bool = True, raise_on_auth_failed: bool = False, scheduled: bool = False, raise_on_entry_error: bool = False) -> None: ...
