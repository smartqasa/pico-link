from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.components.recorder.models import bytes_to_ulid_or_none as bytes_to_ulid_or_none, bytes_to_uuid_hex_or_none as bytes_to_uuid_hex_or_none, ulid_to_bytes_or_none as ulid_to_bytes_or_none, uuid_hex_to_bytes_or_none as uuid_hex_to_bytes_or_none
from homeassistant.const import ATTR_ICON as ATTR_ICON, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.core import Context as Context, Event as Event, State as State, callback as callback
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.json import json_loads as json_loads
from homeassistant.util.ulid import ulid_to_bytes as ulid_to_bytes
from propcache import cached_property
from sqlalchemy.engine.row import Row as Row
from typing import Any, Final, NamedTuple

@dataclass(slots=True)
class LogbookConfig:
    external_events: dict[EventType[Any] | str, tuple[str, Callable[[LazyEventPartialState], dict[str, Any]]]]
    sqlalchemy_filter: Filters | None = ...
    entity_filter: Callable[[str], bool] | None = ...

class LazyEventPartialState:
    row: Incomplete
    data: Incomplete
    def __init__(self, row: Row | EventAsRow, event_data_cache: dict[str, dict[str, Any]]) -> None: ...
    @cached_property
    def event_type(self) -> EventType[Any] | str | None: ...
    @cached_property
    def entity_id(self) -> str | None: ...
    @cached_property
    def state(self) -> str | None: ...
    @cached_property
    def context_id(self) -> str | None: ...
    @cached_property
    def context_user_id(self) -> str | None: ...
    @cached_property
    def context_parent_id(self) -> str | None: ...

ROW_ID_POS: Final[int]
EVENT_TYPE_POS: Final[int]
EVENT_DATA_POS: Final[int]
TIME_FIRED_TS_POS: Final[int]
CONTEXT_ID_BIN_POS: Final[int]
CONTEXT_USER_ID_BIN_POS: Final[int]
CONTEXT_PARENT_ID_BIN_POS: Final[int]
STATE_POS: Final[int]
ENTITY_ID_POS: Final[int]
ICON_POS: Final[int]
CONTEXT_ONLY_POS: Final[int]
DATA_POS: Final[int]
CONTEXT_POS: Final[int]

class EventAsRow(NamedTuple):
    row_id: int
    event_type: EventType[Any] | str | None
    event_data: str | None
    time_fired_ts: float
    context_id_bin: bytes
    context_user_id_bin: bytes | None
    context_parent_id_bin: bytes | None
    state: str | None
    entity_id: str | None
    icon: str | None
    context_only: bool | None
    data: Mapping[str, Any]
    context: Context

@callback
def async_event_to_row(event: Event) -> EventAsRow: ...
