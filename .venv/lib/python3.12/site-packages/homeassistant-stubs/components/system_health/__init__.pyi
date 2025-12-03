import dataclasses
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client, integration_platform as integration_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Protocol

_LOGGER: Incomplete
DOMAIN: str
INFO_CALLBACK_TIMEOUT: int
CONFIG_SCHEMA: Incomplete

class SystemHealthProtocol(Protocol):
    def async_register(self, hass: HomeAssistant, register: SystemHealthRegistration) -> None: ...

@bind_hass
@callback
def async_register_info(hass: HomeAssistant, domain: str, info_callback: Callable[[HomeAssistant], Awaitable[dict]]) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _register_system_health_platform(hass: HomeAssistant, integration_domain: str, platform: SystemHealthProtocol) -> None: ...
async def get_integration_info(hass: HomeAssistant, registration: SystemHealthRegistration) -> dict[str, Any]: ...
@callback
def _format_value(val: Any) -> Any: ...
@websocket_api.async_response
async def handle_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

@dataclasses.dataclass(slots=True)
class SystemHealthRegistration:
    hass: HomeAssistant
    domain: str
    info_callback: Callable[[HomeAssistant], Awaitable[dict]] | None = ...
    manage_url: str | None = ...
    @callback
    def async_register_info(self, info_callback: Callable[[HomeAssistant], Awaitable[dict]], manage_url: str | None = None) -> None: ...

async def async_check_can_reach_url(hass: HomeAssistant, url: str, more_info: str | None = None) -> str | dict[str, str]: ...
