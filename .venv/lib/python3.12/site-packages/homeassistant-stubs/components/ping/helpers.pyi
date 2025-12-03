from .const import ICMP_TIMEOUT as ICMP_TIMEOUT, PING_TIMEOUT as PING_TIMEOUT
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

_LOGGER: Incomplete
PING_MATCHER: Incomplete
PING_MATCHER_BUSYBOX: Incomplete
WIN32_PING_MATCHER: Incomplete

class PingData:
    data: dict[str, Any] | None
    is_alive: bool
    hass: Incomplete
    ip_address: Incomplete
    _count: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, count: int) -> None: ...

class PingDataICMPLib(PingData):
    _privileged: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, count: int, privileged: bool | None) -> None: ...
    is_alive: bool
    data: Incomplete
    async def async_update(self) -> None: ...

class PingDataSubProcess(PingData):
    _ping_cmd: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, count: int, privileged: bool | None) -> None: ...
    async def async_ping(self) -> dict[str, Any] | None: ...
    data: Incomplete
    is_alive: Incomplete
    async def async_update(self) -> None: ...
