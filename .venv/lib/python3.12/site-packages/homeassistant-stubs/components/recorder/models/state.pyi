from .state_attributes import decode_attributes_from_source as decode_attributes_from_source
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.const import COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import Context as Context, State as State
from propcache import cached_property
from sqlalchemy.engine.row import Row as Row
from typing import Any

_LOGGER: Incomplete
EMPTY_CONTEXT: Incomplete

def extract_metadata_ids(entity_id_to_metadata_id: dict[str, int | None]) -> list[int]: ...

class LazyState(State):
    _row: Incomplete
    entity_id: Incomplete
    state: Incomplete
    _attributes: dict[str, Any] | None
    _last_updated_ts: float | None
    attr_cache: Incomplete
    context: Incomplete
    def __init__(self, row: Row, attr_cache: dict[str, dict[str, Any]], start_time_ts: float | None, entity_id: str, state: str, last_updated_ts: float | None, no_attributes: bool) -> None: ...
    @cached_property
    def attributes(self) -> dict[str, Any]: ...
    @cached_property
    def _last_changed_ts(self) -> float | None: ...
    @cached_property
    def last_changed(self) -> datetime: ...
    @cached_property
    def _last_reported_ts(self) -> float | None: ...
    @cached_property
    def last_reported(self) -> datetime: ...
    @cached_property
    def last_updated(self) -> datetime: ...
    @cached_property
    def last_updated_timestamp(self) -> float: ...
    @cached_property
    def last_changed_timestamp(self) -> float: ...
    @cached_property
    def last_reported_timestamp(self) -> float: ...
    def as_dict(self) -> dict[str, Any]: ...

def row_to_compressed_state(row: Row, attr_cache: dict[str, dict[str, Any]], start_time_ts: float | None, entity_id: str, state: str, last_updated_ts: float | None, no_attributes: bool) -> dict[str, Any]: ...
