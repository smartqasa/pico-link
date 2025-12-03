from .all import all_stmt as all_stmt
from .devices import devices_stmt as devices_stmt
from .entities import entities_stmt as entities_stmt
from .entities_and_devices import entities_devices_stmt as entities_devices_stmt
from collections.abc import Collection
from datetime import datetime as dt
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.components.recorder.models import ulid_to_bytes_or_none as ulid_to_bytes_or_none
from homeassistant.helpers.json import json_dumps as json_dumps
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement

def statement_for_request(start_day_dt: dt, end_day_dt: dt, event_type_ids: tuple[int, ...], entity_ids: list[str] | None = None, states_metadata_ids: Collection[int] | None = None, device_ids: list[str] | None = None, filters: Filters | None = None, context_id: str | None = None) -> StatementLambdaElement: ...
