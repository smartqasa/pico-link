import voluptuous as vol
from . import const as const, messages as messages
from .http import WebSocketAdapter as WebSocketAdapter
from .messages import error_message as error_message, event_message as event_message, message_to_json_bytes as message_to_json_bytes, result_message as result_message
from .util import describe_request as describe_request
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable, Hashable
from homeassistant.auth.models import RefreshToken as RefreshToken, User as User
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized
from homeassistant.helpers.http import current_request as current_request
from homeassistant.util.json import JsonValueType as JsonValueType
from typing import Any, Literal

current_connection: Incomplete
type MessageHandler = Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], None]
type BinaryHandler = Callable[[HomeAssistant, ActiveConnection, bytes], None]

class ActiveConnection:
    __slots__: Incomplete
    logger: Incomplete
    hass: Incomplete
    send_message: Incomplete
    user: Incomplete
    refresh_token_id: Incomplete
    subscriptions: dict[Hashable, Callable[[], Any]]
    last_id: int
    can_coalesce: bool
    supported_features: dict[str, float]
    handlers: dict[str, tuple[MessageHandler, vol.Schema | Literal[False]]]
    binary_handlers: list[BinaryHandler | None]
    def __init__(self, logger: WebSocketAdapter, hass: HomeAssistant, send_message: Callable[[bytes | str | dict[str, Any]], None], user: User, refresh_token: RefreshToken) -> None: ...
    def __repr__(self) -> str: ...
    def set_supported_features(self, features: dict[str, float]) -> None: ...
    def get_description(self, request: web.Request | None) -> str: ...
    def context(self, msg: dict[str, Any]) -> Context: ...
    @callback
    def async_register_binary_handler(self, handler: BinaryHandler) -> tuple[int, Callable[[], None]]: ...
    @callback
    def send_result(self, msg_id: int, result: Any | None = None) -> None: ...
    @callback
    def send_event(self, msg_id: int, event: Any | None = None) -> None: ...
    @callback
    def send_error(self, msg_id: int, code: str, message: str, translation_key: str | None = None, translation_domain: str | None = None, translation_placeholders: dict[str, Any] | None = None) -> None: ...
    @callback
    def async_handle_binary(self, handler_id: int, payload: bytes) -> None: ...
    @callback
    def async_handle(self, msg: JsonValueType) -> None: ...
    @callback
    def async_handle_close(self) -> None: ...
    @callback
    def _connect_closed_error(self, msg: bytes | str | dict[str, Any] | Callable[[], str]) -> None: ...
    @callback
    def async_handle_exception(self, msg: dict[str, Any], err: Exception) -> None: ...
