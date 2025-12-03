from .const import F_SERIES as F_SERIES
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntityDescription as NumberEntityDescription
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.const import Platform as Platform
from myuplink import DevicePoint as DevicePoint

def find_matching_platform(device_point: DevicePoint, description: SensorEntityDescription | NumberEntityDescription | None = None) -> Platform: ...

WEEKDAYS: Incomplete
PARAMETER_ID_TO_EXCLUDE_F730: Incomplete
PARAMETER_ID_TO_INCLUDE_SMO20: Incomplete

def skip_entity(model: str, device_point: DevicePoint) -> bool: ...
def transform_model_series(prefix: str) -> str: ...
