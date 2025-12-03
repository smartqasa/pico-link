import datetime
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.template import Template as Template

_LOGGER: Incomplete
DURATION_START: str
DURATION_END: str

@callback
def async_calculate_period(duration: datetime.timedelta | None, start_template: Template | None, end_template: Template | None) -> tuple[datetime.datetime, datetime.datetime]: ...
def pretty_ratio(value: float, period: tuple[datetime.datetime, datetime.datetime]) -> float: ...
def floored_timestamp(incoming_dt: datetime.datetime) -> float: ...
