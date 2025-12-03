from . import PLATFORMS as PLATFORMS
from .const import CONF_ENTITY_IDS as CONF_ENTITY_IDS, CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from typing import Any

_LOGGER: Incomplete
ATTR_MIN_VALUE: str
ATTR_MIN_ENTITY_ID: str
ATTR_MAX_VALUE: str
ATTR_MAX_ENTITY_ID: str
ATTR_MEAN: str
ATTR_MEDIAN: str
ATTR_LAST: str
ATTR_LAST_ENTITY_ID: str
ATTR_RANGE: str
ATTR_SUM: str
ICON: str
SENSOR_TYPES: Incomplete
SENSOR_TYPE_TO_ATTR: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
def calc_min(sensor_values: list[tuple[str, Any]]) -> tuple[str | None, float | None]: ...
def calc_max(sensor_values: list[tuple[str, Any]]) -> tuple[str | None, float | None]: ...
def calc_mean(sensor_values: list[tuple[str, Any]], round_digits: int) -> float | None: ...
def calc_median(sensor_values: list[tuple[str, Any]], round_digits: int) -> float | None: ...
def calc_range(sensor_values: list[tuple[str, Any]], round_digits: int) -> float | None: ...
def calc_sum(sensor_values: list[tuple[str, Any]], round_digits: int) -> float | None: ...

class MinMaxSensor(SensorEntity):
    _attr_icon = ICON
    _attr_should_poll: bool
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _entity_ids: Incomplete
    _sensor_type: Incomplete
    _round_digits: Incomplete
    _attr_name: Incomplete
    _sensor_attr: Incomplete
    _unit_of_measurement: Incomplete
    _unit_of_measurement_mismatch: bool
    min_value: float | None
    max_value: float | None
    mean: float | None
    last: float | None
    median: float | None
    range: float | None
    sum: float | None
    min_entity_id: str | None
    max_entity_id: str | None
    last_entity_id: str | None
    count_sensors: Incomplete
    states: dict[str, Any]
    def __init__(self, entity_ids: list[str], name: str | None, sensor_type: str, round_digits: int, unique_id: str | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @callback
    def _async_min_max_sensor_state_listener(self, event: Event[EventStateChangedData], update_state: bool = True) -> None: ...
    @callback
    def _calc_values(self) -> None: ...
