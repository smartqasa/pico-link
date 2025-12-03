from . import SensorDeviceClass as SensorDeviceClass
from _typeshed import Incomplete
from datetime import date, datetime
from homeassistant.core import callback as callback

_LOGGER: Incomplete

@callback
def async_parse_date_datetime(value: str, entity_id: str, device_class: SensorDeviceClass | str | None) -> datetime | date | None: ...
