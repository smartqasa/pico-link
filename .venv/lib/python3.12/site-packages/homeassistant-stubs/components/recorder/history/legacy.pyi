from ..db_schema import StateAttributes as StateAttributes, States as States
from ..filters import Filters as Filters
from ..models import process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from ..models.legacy import LegacyLazyState as LegacyLazyState, legacy_row_to_compressed_state as legacy_row_to_compressed_state
from ..util import execute_stmt_lambda_element as execute_stmt_lambda_element, session_scope as session_scope
from .const import LAST_CHANGED_KEY as LAST_CHANGED_KEY, NEED_ATTRIBUTE_DOMAINS as NEED_ATTRIBUTE_DOMAINS, SIGNIFICANT_DOMAINS as SIGNIFICANT_DOMAINS, SIGNIFICANT_DOMAINS_ENTITY_ID_LIKE as SIGNIFICANT_DOMAINS_ENTITY_ID_LIKE, STATE_KEY as STATE_KEY
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from datetime import datetime
from homeassistant.const import COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, split_entity_id as split_entity_id
from homeassistant.helpers.recorder import get_instance as get_instance
from sqlalchemy import Column as Column
from sqlalchemy.engine.row import Row as Row
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from typing import Any

_BASE_STATES: Incomplete
_BASE_STATES_NO_LAST_CHANGED: Incomplete
_QUERY_STATE_NO_ATTR: Incomplete
_QUERY_STATE_NO_ATTR_NO_LAST_CHANGED: Incomplete
_BASE_STATES_PRE_SCHEMA_31: Incomplete
_BASE_STATES_NO_LAST_CHANGED_PRE_SCHEMA_31: Incomplete
_QUERY_STATE_NO_ATTR_PRE_SCHEMA_31: Incomplete
_QUERY_STATE_NO_ATTR_NO_LAST_CHANGED_PRE_SCHEMA_31: Incomplete
_QUERY_STATES_PRE_SCHEMA_25: Incomplete
_QUERY_STATES_PRE_SCHEMA_25_NO_LAST_CHANGED: Incomplete
_QUERY_STATES_PRE_SCHEMA_31: Incomplete
_QUERY_STATES_NO_LAST_CHANGED_PRE_SCHEMA_31: Incomplete
_QUERY_STATES: Incomplete
_QUERY_STATES_NO_LAST_CHANGED: Incomplete
_FIELD_MAP: Incomplete
_FIELD_MAP_PRE_SCHEMA_31: Incomplete

def _lambda_stmt_and_join_attributes(no_attributes: bool, include_last_changed: bool = True) -> tuple[StatementLambdaElement, bool]: ...
def get_significant_states(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, minimal_response: bool = False, no_attributes: bool = False, compressed_state_format: bool = False) -> dict[str, list[State | dict[str, Any]]]: ...
def _significant_states_stmt(start_time: datetime, end_time: datetime | None, entity_ids: list[str], significant_changes_only: bool, no_attributes: bool) -> StatementLambdaElement: ...
def get_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, minimal_response: bool = False, no_attributes: bool = False, compressed_state_format: bool = False) -> dict[str, list[State | dict[str, Any]]]: ...
def get_full_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, no_attributes: bool = False) -> dict[str, list[State]]: ...
def _state_changed_during_period_stmt(start_time: datetime, end_time: datetime | None, entity_id: str, no_attributes: bool, descending: bool, limit: int | None) -> StatementLambdaElement: ...
def state_changes_during_period(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = None, entity_id: str | None = None, no_attributes: bool = False, descending: bool = False, limit: int | None = None, include_start_time_state: bool = True) -> dict[str, list[State]]: ...
def _get_last_state_changes_stmt(number_of_states: int, entity_id: str) -> StatementLambdaElement: ...
def get_last_state_changes(hass: HomeAssistant, number_of_states: int, entity_id: str) -> dict[str, list[State]]: ...
def _get_states_for_entities_stmt(run_start_ts: float, utc_point_in_time: datetime, entity_ids: list[str], no_attributes: bool) -> StatementLambdaElement: ...
def _get_rows_with_session(hass: HomeAssistant, session: Session, utc_point_in_time: datetime, entity_ids: list[str], *, no_attributes: bool = False) -> Iterable[Row]: ...
def _get_single_entity_states_stmt(utc_point_in_time: datetime, entity_id: str, no_attributes: bool = False) -> StatementLambdaElement: ...
def _sorted_states_to_dict(hass: HomeAssistant, session: Session, states: Iterable[Row], start_time: datetime, entity_ids: list[str], include_start_time_state: bool = True, minimal_response: bool = False, no_attributes: bool = False, compressed_state_format: bool = False) -> dict[str, list[State | dict[str, Any]]]: ...
