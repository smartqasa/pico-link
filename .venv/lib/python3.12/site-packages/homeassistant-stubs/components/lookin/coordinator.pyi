from .const import NEVER_TIME as NEVER_TIME, POLLING_FALLBACK_SECONDS as POLLING_FALLBACK_SECONDS
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class LookinPushCoordinator:
    last_update: Incomplete
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def update(self) -> None: ...
    def active(self, interval: timedelta) -> bool: ...

class LookinDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT]):
    push_coordinator: Incomplete
    def __init__(self, hass: HomeAssistant, push_coordinator: LookinPushCoordinator, name: str, update_interval: timedelta | None = None, update_method: Callable[[], Awaitable[_DataT]] | None = None) -> None: ...
    @callback
    def async_set_updated_data(self, data: _DataT) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
