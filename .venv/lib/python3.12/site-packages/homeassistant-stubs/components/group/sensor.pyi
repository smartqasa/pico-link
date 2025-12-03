from .const import CONF_IGNORE_NON_NUMERIC as CONF_IGNORE_NON_NUMERIC
from .entity import GroupEntity as GroupEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass, UNIT_CONVERTERS as UNIT_CONVERTERS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import get_capability as get_capability, get_device_class as get_device_class, get_unit_of_measurement as get_unit_of_measurement
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from typing import Any

DEFAULT_NAME: str
ATTR_MIN_VALUE: str
ATTR_MIN_ENTITY_ID: str
ATTR_MAX_VALUE: str
ATTR_MAX_ENTITY_ID: str
ATTR_MEAN: str
ATTR_MEDIAN: str
ATTR_LAST: str
ATTR_LAST_ENTITY_ID: str
ATTR_RANGE: str
ATTR_STDEV: str
ATTR_SUM: str
ATTR_PRODUCT: str
SENSOR_TYPES: Incomplete
SENSOR_TYPE_TO_ATTR: Incomplete
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_sensor(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> SensorGroup: ...
def _has_numeric_state(hass: HomeAssistant, entity_id: str) -> bool: ...
def calc_min(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_max(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_mean(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_median(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_last(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_range(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float]: ...
def calc_stdev(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float]: ...
def calc_sum(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float]: ...
def calc_product(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float]: ...

CALC_TYPES: dict[str, Callable[[list[tuple[str, float, State]]], tuple[dict[str, str | None], float | None]]]

class SensorGroup(GroupEntity, SensorEntity):
    _attr_available: bool
    _attr_should_poll: bool
    hass: Incomplete
    _entity_ids: Incomplete
    _sensor_type: Incomplete
    _configured_state_class: Incomplete
    _configured_device_class: Incomplete
    _configured_unit_of_measurement: Incomplete
    _valid_units: set[str | None]
    _can_convert: bool
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _ignore_non_numeric: Incomplete
    mode: Incomplete
    _state_calc: Callable[[list[tuple[str, float, State]]], tuple[dict[str, str | None], float | None]]
    _state_incorrect: set[str]
    _extra_state_attribute: dict[str, Any]
    def __init__(self, hass: HomeAssistant, unique_id: str | None, name: str, entity_ids: list[str], ignore_non_numeric: bool, sensor_type: str, unit_of_measurement: str | None, state_class: SensorStateClass | None, device_class: SensorDeviceClass | None) -> None: ...
    _attr_state_class: Incomplete
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def calculate_state_attributes(self, valid_state_entities: list[str]) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def async_update_group_state(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str | None: ...
    def _calculate_state_class(self, state_class: SensorStateClass | None, valid_state_entities: list[str]) -> SensorStateClass | None: ...
    def _calculate_device_class(self, device_class: SensorDeviceClass | None, valid_state_entities: list[str]) -> SensorDeviceClass | None: ...
    def _calculate_unit_of_measurement(self, unit_of_measurement: str | None, valid_state_entities: list[str]) -> str | None: ...
    def _get_valid_units(self) -> set[str | None]: ...
    def _get_valid_entities(self) -> list[str]: ...
