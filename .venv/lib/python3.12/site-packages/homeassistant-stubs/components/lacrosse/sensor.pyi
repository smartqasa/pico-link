import pylacrosse
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import async_generate_entity_id as async_generate_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
CONF_BAUD: str
CONF_DATARATE: str
CONF_EXPIRE_AFTER: str
CONF_FREQUENCY: str
CONF_JEELINK_LED: str
CONF_TOGGLE_INTERVAL: str
CONF_TOGGLE_MASK: str
DEFAULT_DEVICE: str
DEFAULT_BAUD: int
DEFAULT_EXPIRE_AFTER: int
TYPES: Incomplete
SENSOR_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class LaCrosseSensor(SensorEntity):
    _temperature: float | None
    _humidity: int | None
    _low_battery: bool | None
    _new_battery: bool | None
    hass: Incomplete
    entity_id: Incomplete
    _config: Incomplete
    _expire_after: Incomplete
    _expiration_trigger: CALLBACK_TYPE | None
    _attr_name: Incomplete
    def __init__(self, hass: HomeAssistant, lacrosse: pylacrosse.LaCrosse, device_id: str, name: str, expire_after: int | None, config: ConfigType) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _callback_lacrosse(self, lacrosse_sensor: pylacrosse.LaCrosseSensor, user_data: None) -> None: ...
    @callback
    def value_is_expired(self, *_: datetime) -> None: ...

class LaCrosseTemperature(LaCrosseSensor):
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @property
    def native_value(self) -> float | None: ...

class LaCrosseHumidity(LaCrosseSensor):
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class: Incomplete
    _attr_device_class: Incomplete
    @property
    def native_value(self) -> int | None: ...

class LaCrosseBattery(LaCrosseSensor):
    @property
    def native_value(self) -> str | None: ...
    @property
    def icon(self) -> str: ...

TYPE_CLASSES: dict[str, type[LaCrosseSensor]]
