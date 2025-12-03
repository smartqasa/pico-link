from .connection import ActiveConnection as ActiveConnection
from .error import Disconnect as Disconnect
from .http import WebSocketAdapter as WebSocketAdapter
from _typeshed import Incomplete
from aiohttp.web import Request as Request
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.http.ban import process_success_login as process_success_login, process_wrong_login as process_wrong_login
from homeassistant.const import __version__ as __version__
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.json import json_bytes as json_bytes
from homeassistant.util.json import JsonValueType as JsonValueType
from typing import Any, Final

TYPE_AUTH: Final[str]
TYPE_AUTH_INVALID: Final[str]
TYPE_AUTH_OK: Final[str]
TYPE_AUTH_REQUIRED: Final[str]
AUTH_MESSAGE_SCHEMA: Final[Incomplete]
AUTH_OK_MESSAGE: Incomplete
AUTH_REQUIRED_MESSAGE: Incomplete

def auth_invalid_message(message: str) -> bytes: ...

class AuthPhase:
    _hass: Incomplete
    _send_message: Incomplete
    _cancel_ws: Incomplete
    _logger: Incomplete
    _request: Incomplete
    _send_bytes_text: Incomplete
    def __init__(self, logger: WebSocketAdapter, hass: HomeAssistant, send_message: Callable[[bytes | str | dict[str, Any]], None], cancel_ws: CALLBACK_TYPE, request: Request, send_bytes_text: Callable[[bytes], Coroutine[Any, Any, None]]) -> None: ...
    async def async_handle(self, msg: JsonValueType) -> ActiveConnection: ...
