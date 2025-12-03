from _typeshed import Incomplete
from aiohttp import StreamReader as StreamReader
from aiohttp.web import Request, Response
from collections.abc import Awaitable, Callable as Callable, Iterable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.network import get_url as get_url, is_cloud_connection as is_cloud_connection
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import network as network
from homeassistant.util.aiohttp import MockRequest as MockRequest, MockStreamReader as MockStreamReader, serialize_response as serialize_response
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
DEFAULT_METHODS: Incomplete
SUPPORTED_METHODS: Incomplete
URL_WEBHOOK_PATH: str
CONFIG_SCHEMA: Incomplete

@callback
@bind_hass
def async_register(hass: HomeAssistant, domain: str, name: str, webhook_id: str, handler: Callable[[HomeAssistant, str, Request], Awaitable[Response | None]], *, local_only: bool | None = False, allowed_methods: Iterable[str] | None = None) -> None: ...
@callback
@bind_hass
def async_unregister(hass: HomeAssistant, webhook_id: str) -> None: ...
@callback
def async_generate_id() -> str: ...
@callback
@bind_hass
def async_generate_url(hass: HomeAssistant, webhook_id: str, allow_internal: bool = True, allow_external: bool = True, allow_ip: bool | None = None, prefer_external: bool | None = True) -> str: ...
@callback
def async_generate_path(webhook_id: str) -> str: ...
@bind_hass
async def async_handle_webhook(hass: HomeAssistant, webhook_id: str, request: Request | MockRequest) -> Response: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class WebhookView(HomeAssistantView):
    url = URL_WEBHOOK_PATH
    name: str
    requires_auth: bool
    cors_allowed: bool
    async def _handle(self, request: Request, webhook_id: str) -> Response: ...
    get = _handle
    head = _handle
    post = _handle
    put = _handle

@callback
def websocket_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_handle(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
