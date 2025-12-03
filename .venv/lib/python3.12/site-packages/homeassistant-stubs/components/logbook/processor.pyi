from .const import ATTR_MESSAGE as ATTR_MESSAGE, CONTEXT_DOMAIN as CONTEXT_DOMAIN, CONTEXT_ENTITY_ID as CONTEXT_ENTITY_ID, CONTEXT_ENTITY_ID_NAME as CONTEXT_ENTITY_ID_NAME, CONTEXT_EVENT_TYPE as CONTEXT_EVENT_TYPE, CONTEXT_MESSAGE as CONTEXT_MESSAGE, CONTEXT_NAME as CONTEXT_NAME, CONTEXT_SERVICE as CONTEXT_SERVICE, CONTEXT_SOURCE as CONTEXT_SOURCE, CONTEXT_STATE as CONTEXT_STATE, CONTEXT_USER_ID as CONTEXT_USER_ID, DOMAIN as DOMAIN, LOGBOOK_ENTRY_DOMAIN as LOGBOOK_ENTRY_DOMAIN, LOGBOOK_ENTRY_ENTITY_ID as LOGBOOK_ENTRY_ENTITY_ID, LOGBOOK_ENTRY_ICON as LOGBOOK_ENTRY_ICON, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME, LOGBOOK_ENTRY_SOURCE as LOGBOOK_ENTRY_SOURCE, LOGBOOK_ENTRY_STATE as LOGBOOK_ENTRY_STATE, LOGBOOK_ENTRY_WHEN as LOGBOOK_ENTRY_WHEN
from .helpers import is_sensor_continuous as is_sensor_continuous
from .models import CONTEXT_ID_BIN_POS as CONTEXT_ID_BIN_POS, CONTEXT_ONLY_POS as CONTEXT_ONLY_POS, CONTEXT_PARENT_ID_BIN_POS as CONTEXT_PARENT_ID_BIN_POS, CONTEXT_POS as CONTEXT_POS, CONTEXT_USER_ID_BIN_POS as CONTEXT_USER_ID_BIN_POS, ENTITY_ID_POS as ENTITY_ID_POS, EVENT_TYPE_POS as EVENT_TYPE_POS, EventAsRow as EventAsRow, ICON_POS as ICON_POS, LazyEventPartialState as LazyEventPartialState, LogbookConfig as LogbookConfig, ROW_ID_POS as ROW_ID_POS, STATE_POS as STATE_POS, TIME_FIRED_TS_POS as TIME_FIRED_TS_POS, async_event_to_row as async_event_to_row
from .queries import statement_for_request as statement_for_request
from .queries.common import PSEUDO_EVENT_STATE_CHANGED as PSEUDO_EVENT_STATE_CHANGED
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator, Sequence
from dataclasses import dataclass
from datetime import datetime as dt
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.components.recorder.models import bytes_to_uuid_hex_or_none as bytes_to_uuid_hex_or_none, extract_event_type_ids as extract_event_type_ids, extract_metadata_ids as extract_metadata_ids, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from homeassistant.components.recorder.util import execute_stmt_lambda_element as execute_stmt_lambda_element, session_scope as session_scope
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_NAME as ATTR_NAME, ATTR_SERVICE as ATTR_SERVICE, EVENT_CALL_SERVICE as EVENT_CALL_SERVICE, EVENT_LOGBOOK_ENTRY as EVENT_LOGBOOK_ENTRY
from homeassistant.core import HomeAssistant as HomeAssistant, split_entity_id as split_entity_id
from homeassistant.helpers import entity_registry as er
from homeassistant.util.event_type import EventType as EventType
from sqlalchemy.engine import Result as Result
from sqlalchemy.engine.row import Row as Row
from typing import Any

_LOGGER: Incomplete

@dataclass(slots=True)
class LogbookRun:
    context_lookup: dict[bytes | None, Row | EventAsRow | None]
    external_events: dict[EventType[Any] | str, tuple[str, Callable[[LazyEventPartialState], dict[str, Any]]]]
    event_cache: EventCache
    entity_name_cache: EntityNameCache
    include_entity_name: bool
    timestamp: bool
    memoize_new_contexts: bool = ...

class EventProcessor:
    hass: Incomplete
    ent_reg: Incomplete
    event_types: Incomplete
    entity_ids: Incomplete
    device_ids: Incomplete
    context_id: Incomplete
    filters: Filters | None
    logbook_run: Incomplete
    context_augmenter: Incomplete
    def __init__(self, hass: HomeAssistant, event_types: tuple[EventType[Any] | str, ...], entity_ids: list[str] | None = None, device_ids: list[str] | None = None, context_id: str | None = None, timestamp: bool = False, include_entity_name: bool = True) -> None: ...
    @property
    def limited_select(self) -> bool: ...
    def switch_to_live(self) -> None: ...
    def get_events(self, start_day: dt, end_day: dt) -> list[dict[str, Any]]: ...
    def humanify(self, rows: Generator[EventAsRow] | Sequence[Row] | Result) -> list[dict[str, str]]: ...

def _humanify(hass: HomeAssistant, rows: Generator[EventAsRow] | Sequence[Row] | Result, ent_reg: er.EntityRegistry, logbook_run: LogbookRun, context_augmenter: ContextAugmenter) -> Generator[dict[str, Any]]: ...

class ContextAugmenter:
    context_lookup: Incomplete
    entity_name_cache: Incomplete
    external_events: Incomplete
    event_cache: Incomplete
    include_entity_name: Incomplete
    def __init__(self, logbook_run: LogbookRun) -> None: ...
    def get_context(self, context_id_bin: bytes | None, row: Row | EventAsRow | None) -> Row | EventAsRow | None: ...
    def augment(self, data: dict[str, Any], context_row: Row | EventAsRow) -> None: ...

def _rows_ids_match(row: Row | EventAsRow, other_row: Row | EventAsRow) -> bool: ...

class EntityNameCache:
    _hass: Incomplete
    _names: dict[str, str]
    def __init__(self, hass: HomeAssistant) -> None: ...
    def get(self, entity_id: str) -> str: ...

class EventCache:
    _event_data_cache: Incomplete
    event_cache: dict[Row | EventAsRow, LazyEventPartialState]
    def __init__(self, event_data_cache: dict[str, dict[str, Any]]) -> None: ...
    def get(self, row: EventAsRow | Row) -> LazyEventPartialState: ...
    def clear(self) -> None: ...
