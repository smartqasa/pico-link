import logging
import re
from _typeshed import Incomplete
from collections import OrderedDict
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from types import FrameType
from typing import Any

type KeyType = tuple[str, tuple[str, int], tuple[str, int, str] | None]
CONF_MAX_ENTRIES: str
CONF_FIRE_EVENT: str
CONF_MESSAGE: str
CONF_LEVEL: str
CONF_LOGGER: str
DATA_SYSTEM_LOG: str
DEFAULT_MAX_ENTRIES: int
DEFAULT_FIRE_EVENT: bool
DOMAIN: str
EVENT_SYSTEM_LOG: str
SERVICE_CLEAR: str
SERVICE_WRITE: str
CONFIG_SCHEMA: Incomplete
SERVICE_CLEAR_SCHEMA: Incomplete
SERVICE_WRITE_SCHEMA: Incomplete

def _figure_out_source(record: logging.LogRecord, paths_re: re.Pattern[str], extracted_tb: list[tuple[FrameType, int]] | None = None) -> tuple[str, int]: ...
def _safe_get_message(record: logging.LogRecord) -> str: ...

class LogEntry:
    __slots__: Incomplete
    first_occurred: Incomplete
    name: Incomplete
    level: Incomplete
    message: Incomplete
    exception: str
    root_cause: tuple[str, int, str] | None
    source: Incomplete
    count: int
    key: Incomplete
    def __init__(self, record: logging.LogRecord, paths_re: re.Pattern, formatter: logging.Formatter | None = None, figure_out_source: bool = False) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class DedupStore(OrderedDict[KeyType, LogEntry]):
    maxlen: Incomplete
    def __init__(self, maxlen: int = 50) -> None: ...
    def add_entry(self, entry: LogEntry) -> None: ...
    def to_list(self) -> list[dict[str, Any]]: ...

class LogErrorHandler(logging.Handler):
    hass: Incomplete
    records: Incomplete
    fire_event: Incomplete
    paths_re: Incomplete
    def __init__(self, hass: HomeAssistant, maxlen: int, fire_event: bool, paths_re: re.Pattern[str]) -> None: ...
    def emit(self, record: logging.LogRecord) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@websocket_api.require_admin
@callback
def list_errors(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
