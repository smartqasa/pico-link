from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_ACTIVE as CHAR_ACTIVE, CHAR_COOLING_THRESHOLD_TEMPERATURE as CHAR_COOLING_THRESHOLD_TEMPERATURE, CHAR_CURRENT_FAN_STATE as CHAR_CURRENT_FAN_STATE, CHAR_CURRENT_HEATING_COOLING as CHAR_CURRENT_HEATING_COOLING, CHAR_CURRENT_HUMIDITY as CHAR_CURRENT_HUMIDITY, CHAR_CURRENT_TEMPERATURE as CHAR_CURRENT_TEMPERATURE, CHAR_HEATING_THRESHOLD_TEMPERATURE as CHAR_HEATING_THRESHOLD_TEMPERATURE, CHAR_ROTATION_SPEED as CHAR_ROTATION_SPEED, CHAR_SWING_MODE as CHAR_SWING_MODE, CHAR_TARGET_FAN_STATE as CHAR_TARGET_FAN_STATE, CHAR_TARGET_HEATING_COOLING as CHAR_TARGET_HEATING_COOLING, CHAR_TARGET_HUMIDITY as CHAR_TARGET_HUMIDITY, CHAR_TARGET_TEMPERATURE as CHAR_TARGET_TEMPERATURE, CHAR_TEMP_DISPLAY_UNITS as CHAR_TEMP_DISPLAY_UNITS, DEFAULT_MAX_TEMP_WATER_HEATER as DEFAULT_MAX_TEMP_WATER_HEATER, DEFAULT_MIN_TEMP_WATER_HEATER as DEFAULT_MIN_TEMP_WATER_HEATER, PROP_MAX_VALUE as PROP_MAX_VALUE, PROP_MIN_STEP as PROP_MIN_STEP, PROP_MIN_VALUE as PROP_MIN_VALUE, SERV_FANV2 as SERV_FANV2, SERV_THERMOSTAT as SERV_THERMOSTAT
from .util import get_min_max as get_min_max, temperature_to_homekit as temperature_to_homekit, temperature_to_states as temperature_to_states
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_CURRENT_TEMPERATURE as ATTR_CURRENT_TEMPERATURE, ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_FAN_MODES as ATTR_FAN_MODES, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_ACTION as ATTR_HVAC_ACTION, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_HVAC_MODES as ATTR_HVAC_MODES, ATTR_MAX_HUMIDITY as ATTR_MAX_HUMIDITY, ATTR_MAX_TEMP as ATTR_MAX_TEMP, ATTR_MIN_HUMIDITY as ATTR_MIN_HUMIDITY, ATTR_MIN_TEMP as ATTR_MIN_TEMP, ATTR_SWING_MODE as ATTR_SWING_MODE, ATTR_SWING_MODES as ATTR_SWING_MODES, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntityFeature as ClimateEntityFeature, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MAX_TEMP as DEFAULT_MAX_TEMP, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_MIDDLE as FAN_MIDDLE, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, SERVICE_SET_FAN_MODE as SERVICE_SET_FAN_MODE, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_SWING_MODE as SERVICE_SET_SWING_MODE, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_ON as SWING_ON, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_TEMPERATURE as ATTR_TEMPERATURE, PERCENTAGE as PERCENTAGE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import State as State, callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item
from typing import Any

_LOGGER: Incomplete
DEFAULT_HVAC_MODES: Incomplete
HC_HOMEKIT_VALID_MODES_WATER_HEATER: Incomplete
UNIT_HASS_TO_HOMEKIT: Incomplete
HC_HEAT_COOL_OFF: int
HC_HEAT_COOL_HEAT: int
HC_HEAT_COOL_COOL: int
HC_HEAT_COOL_AUTO: int
HC_HEAT_COOL_PREFER_HEAT: Incomplete
HC_HEAT_COOL_PREFER_COOL: Incomplete
ORDERED_FAN_SPEEDS: Incomplete
PRE_DEFINED_FAN_MODES: Incomplete
SWING_MODE_PREFERRED_ORDER: Incomplete
PRE_DEFINED_SWING_MODES: Incomplete
HC_MIN_TEMP: int
HC_MAX_TEMP: int
UNIT_HOMEKIT_TO_HASS: Incomplete
HC_HASS_TO_HOMEKIT: Incomplete
HC_HOMEKIT_TO_HASS: Incomplete
HC_HASS_TO_HOMEKIT_ACTION: Incomplete
FAN_STATE_INACTIVE: int
FAN_STATE_IDLE: int
FAN_STATE_ACTIVE: int
HC_HASS_TO_HOMEKIT_FAN_STATE: Incomplete
HEAT_COOL_DEADBAND: int

def _hk_hvac_mode_from_state(state: State) -> int | None: ...

class Thermostat(HomeAccessory):
    _unit: Incomplete
    chars: list[str]
    fan_chars: list[str]
    char_current_heat_cool: Incomplete
    char_target_heat_cool: Incomplete
    char_current_temp: Incomplete
    char_target_temp: Incomplete
    char_display_units: Incomplete
    char_cooling_thresh_temp: Incomplete
    char_heating_thresh_temp: Incomplete
    char_target_humidity: Incomplete
    char_current_humidity: Incomplete
    ordered_fan_speeds: list[str]
    fan_modes: Incomplete
    swing_on_mode: Incomplete
    char_active: Incomplete
    char_swing: Incomplete
    char_speed: Incomplete
    char_current_fan_state: Incomplete
    char_target_fan_state: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def _set_fan_swing_mode(self, swing_on: int) -> None: ...
    def _set_fan_speed(self, speed: int) -> None: ...
    def _get_on_mode(self) -> str: ...
    def _set_fan_active(self, active: int) -> None: ...
    def _set_fan_auto(self, auto: int) -> None: ...
    def _temperature_to_homekit(self, temp: float) -> float: ...
    def _temperature_to_states(self, temp: float) -> float: ...
    def _set_chars(self, char_values: dict[str, Any]) -> None: ...
    hc_homekit_to_hass: Incomplete
    hc_hass_to_homekit: Incomplete
    def _configure_hvac_modes(self, state: State) -> None: ...
    def get_temperature_range(self, state: State) -> tuple[float, float]: ...
    def set_target_humidity(self, value: float) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...
    @callback
    def _async_update_fan_state(self, new_state: State) -> None: ...

class WaterHeater(HomeAccessory):
    _unit: Incomplete
    char_current_heat_cool: Incomplete
    char_target_heat_cool: Incomplete
    char_current_temp: Incomplete
    char_target_temp: Incomplete
    char_display_units: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def get_temperature_range(self, state: State) -> tuple[float, float]: ...
    def set_heat_cool(self, value: int) -> None: ...
    def set_target_temperature(self, value: float) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

def _get_temperature_range_from_state(state: State, unit: str, default_min: float, default_max: float) -> tuple[float, float]: ...
def _get_target_temperature(state: State, unit: str) -> float | None: ...
def _get_current_temperature(state: State, unit: str) -> float | None: ...
