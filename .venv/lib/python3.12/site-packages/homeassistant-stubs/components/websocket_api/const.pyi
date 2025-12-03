from .connection import ActiveConnection as ActiveConnection
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any, Final

type WebSocketCommandHandler = Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], None]
type AsyncWebSocketCommandHandler = Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Awaitable[None]]
DOMAIN: Final[str]
URL: Final[str]
PENDING_MSG_PEAK: Final[int]
PENDING_MSG_PEAK_TIME: Final[int]
MAX_PENDING_MSG: Final[int]
PENDING_MSG_MAX_FORCE_READY: Final[int]
ERR_ID_REUSE: Final[str]
ERR_INVALID_FORMAT: Final[str]
ERR_NOT_ALLOWED: Final[str]
ERR_NOT_FOUND: Final[str]
ERR_NOT_SUPPORTED: Final[str]
ERR_HOME_ASSISTANT_ERROR: Final[str]
ERR_SERVICE_VALIDATION_ERROR: Final[str]
ERR_UNKNOWN_COMMAND: Final[str]
ERR_UNKNOWN_ERROR: Final[str]
ERR_UNAUTHORIZED: Final[str]
ERR_TIMEOUT: Final[str]
ERR_TEMPLATE_ERROR: Final[str]
TYPE_RESULT: Final[str]
SIGNAL_WEBSOCKET_CONNECTED: Final[str]
SIGNAL_WEBSOCKET_DISCONNECTED: Final[str]
DATA_CONNECTIONS: Final[Incomplete]
FEATURE_COALESCE_MESSAGES: str
