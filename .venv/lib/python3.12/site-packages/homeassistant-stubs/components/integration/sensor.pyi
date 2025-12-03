import abc
from .const import CONF_MAX_SUB_INTERVAL as CONF_MAX_SUB_INTERVAL, CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_SOURCE_SENSOR as CONF_SOURCE_SENSOR, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, INTEGRATION_METHODS as INTEGRATION_METHODS, METHOD_LEFT as METHOD_LEFT, METHOD_RIGHT as METHOD_RIGHT, METHOD_TRAPEZOIDAL as METHOD_TRAPEZOIDAL
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from enum import Enum
from homeassistant.components.sensor import DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorExtraStoredData as SensorExtraStoredData, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, UnitOfTime as UnitOfTime
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, EventStateReportedData as EventStateReportedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.device import async_device_info_to_link_from_entity as async_device_info_to_link_from_entity
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_state_change_event as async_track_state_change_event, async_track_state_report_event as async_track_state_report_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final, Self

_LOGGER: Incomplete
ATTR_SOURCE_ID: Final[str]
UNIT_PREFIXES: Incomplete
UNIT_TIME: Incomplete
DEVICE_CLASS_MAP: Incomplete
DEFAULT_ROUND: int
PLATFORM_SCHEMA: Incomplete

class _IntegrationMethod(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    def from_name(method_name: str) -> _IntegrationMethod: ...
    @abstractmethod
    def validate_states(self, left: str, right: str) -> tuple[Decimal, Decimal] | None: ...
    @abstractmethod
    def calculate_area_with_two_states(self, elapsed_time: Decimal, left: Decimal, right: Decimal) -> Decimal: ...
    def calculate_area_with_one_state(self, elapsed_time: Decimal, constant_state: Decimal) -> Decimal: ...

class _Trapezoidal(_IntegrationMethod):
    def calculate_area_with_two_states(self, elapsed_time: Decimal, left: Decimal, right: Decimal) -> Decimal: ...
    def validate_states(self, left: str, right: str) -> tuple[Decimal, Decimal] | None: ...

class _Left(_IntegrationMethod):
    def calculate_area_with_two_states(self, elapsed_time: Decimal, left: Decimal, right: Decimal) -> Decimal: ...
    def validate_states(self, left: str, right: str) -> tuple[Decimal, Decimal] | None: ...

class _Right(_IntegrationMethod):
    def calculate_area_with_two_states(self, elapsed_time: Decimal, left: Decimal, right: Decimal) -> Decimal: ...
    def validate_states(self, left: str, right: str) -> tuple[Decimal, Decimal] | None: ...

def _decimal_state(state: str) -> Decimal | None: ...

_NAME_TO_INTEGRATION_METHOD: dict[str, type[_IntegrationMethod]]

class _IntegrationTrigger(Enum):
    StateEvent = 'state_event'
    TimeElapsed = 'time_elapsed'

@dataclass
class IntegrationSensorExtraStoredData(SensorExtraStoredData):
    source_entity: str | None
    last_valid_state: Decimal | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Self | None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class IntegrationSensor(RestoreSensor):
    _attr_state_class: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _sensor_source_id: Incomplete
    _round_digits: Incomplete
    _state: Decimal | None
    _method: Incomplete
    _attr_name: Incomplete
    _unit_prefix_string: Incomplete
    _unit_of_measurement: str | None
    _unit_prefix: Incomplete
    _unit_time: Incomplete
    _unit_time_str: Incomplete
    _attr_icon: str
    _source_entity: str
    _last_valid_state: Decimal | None
    _attr_device_info: Incomplete
    _max_sub_interval: timedelta | None
    _max_sub_interval_exceeded_callback: CALLBACK_TYPE
    _last_integration_time: datetime
    _last_integration_trigger: Incomplete
    _attr_suggested_display_precision: Incomplete
    def __init__(self, *, integration_method: str, name: str | None, round_digits: int | None, source_entity: str, unique_id: str | None, unit_prefix: str | None, unit_time: UnitOfTime, max_sub_interval: timedelta | None, device_info: DeviceInfo | None = None) -> None: ...
    def _calculate_unit(self, source_unit: str) -> str: ...
    def _calculate_device_class(self, source_device_class: SensorDeviceClass | None, unit_of_measurement: str | None) -> SensorDeviceClass | None: ...
    _attr_device_class: Incomplete
    def _derive_and_set_attributes_from_state(self, source_state: State) -> None: ...
    def _update_integral(self, area: Decimal) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _integrate_on_state_change_with_max_sub_interval(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _integrate_on_state_report_with_max_sub_interval(self, event: Event[EventStateReportedData]) -> None: ...
    @callback
    def _integrate_on_state_update_with_max_sub_interval(self, old_last_reported: datetime | None, old_state: State | None, new_state: State | None) -> None: ...
    @callback
    def _integrate_on_state_change_callback(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _integrate_on_state_report_callback(self, event: Event[EventStateReportedData]) -> None: ...
    _attr_available: bool
    def _integrate_on_state_change(self, old_last_reported: datetime | None, old_state: State | None, new_state: State | None) -> None: ...
    def _schedule_max_sub_interval_exceeded_if_state_is_numeric(self, source_state: State | None) -> None: ...
    def _cancel_max_sub_interval_exceeded_callback(self) -> None: ...
    @property
    def native_value(self) -> Decimal | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    @property
    def extra_restore_state_data(self) -> IntegrationSensorExtraStoredData: ...
    async def async_get_last_sensor_data(self) -> IntegrationSensorExtraStoredData | None: ...
