from .dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send_internal as async_dispatcher_send_internal
from .typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from collections.abc import Callable as Callable, Coroutine
from homeassistant import core as core, setup as setup
from homeassistant.const import Platform as Platform
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.signal_type import SignalTypeFormat as SignalTypeFormat
from typing import Any, TypedDict

SIGNAL_PLATFORM_DISCOVERED: SignalTypeFormat[DiscoveryDict]
EVENT_LOAD_PLATFORM: str
ATTR_PLATFORM: str
ATTR_DISCOVERED: str

class DiscoveryDict(TypedDict):
    service: str
    platform: str | None
    discovered: DiscoveryInfoType | None

@core.callback
@bind_hass
def async_listen(hass: core.HomeAssistant, service: str, callback: Callable[[str, DiscoveryInfoType | None], Coroutine[Any, Any, None] | None]) -> None: ...
@bind_hass
def discover(hass: core.HomeAssistant, service: str, discovered: DiscoveryInfoType, component: str, hass_config: ConfigType) -> None: ...
@bind_hass
async def async_discover(hass: core.HomeAssistant, service: str, discovered: DiscoveryInfoType | None, component: str | None, hass_config: ConfigType) -> None: ...
@bind_hass
def async_listen_platform(hass: core.HomeAssistant, component: str, callback: Callable[[str, dict[str, Any] | None], Any]) -> Callable[[], None]: ...
@bind_hass
def load_platform(hass: core.HomeAssistant, component: Platform | str, platform: str, discovered: DiscoveryInfoType | None, hass_config: ConfigType) -> None: ...
@bind_hass
async def async_load_platform(hass: core.HomeAssistant, component: Platform | str, platform: str, discovered: DiscoveryInfoType | None, hass_config: ConfigType) -> None: ...
