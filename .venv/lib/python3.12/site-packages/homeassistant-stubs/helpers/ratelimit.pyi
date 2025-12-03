import asyncio
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Hashable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete

class KeyedRateLimit:
    hass: Incomplete
    _last_triggered: dict[Hashable, float]
    _rate_limit_timers: dict[Hashable, asyncio.TimerHandle]
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_has_timer(self, key: Hashable) -> bool: ...
    @callback
    def async_triggered(self, key: Hashable, now: float | None = None) -> None: ...
    @callback
    def async_cancel_timer(self, key: Hashable) -> None: ...
    @callback
    def async_remove(self) -> None: ...
    @callback
    def async_schedule_action[*_Ts](self, key: Hashable, rate_limit: float | None, now: float, action: Callable[[*_Ts], None], *args: *_Ts) -> float | None: ...
