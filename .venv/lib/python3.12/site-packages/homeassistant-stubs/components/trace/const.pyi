from .models import TraceData as TraceData
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.hass_dict import HassKey as HassKey

CONF_STORED_TRACES: str
DATA_TRACE: HassKey[TraceData]
DATA_TRACE_STORE: HassKey[Store[dict[str, list]]]
DATA_TRACES_RESTORED: HassKey[bool]
DEFAULT_STORED_TRACES: int
