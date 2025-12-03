import voluptuous as vol
from .const import CONF_INVERT as CONF_INVERT, CONF_KNX_EXPOSE as CONF_KNX_EXPOSE, CONF_PAYLOAD_LENGTH as CONF_PAYLOAD_LENGTH, CONF_RESET_AFTER as CONF_RESET_AFTER, CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, ColorTempModes as ColorTempModes, FanZeroMode as FanZeroMode, KNX_ADDRESS as KNX_ADDRESS
from .validation import backwards_compatible_xknx_climate_enum_member as backwards_compatible_xknx_climate_enum_member, dpt_base_type_validator as dpt_base_type_validator, ga_list_validator as ga_list_validator, ga_validator as ga_validator, numeric_type_validator as numeric_type_validator, sensor_type_validator as sensor_type_validator, string_type_validator as string_type_validator, sync_state_validator as sync_state_validator
from _typeshed import Incomplete
from abc import ABC
from collections import OrderedDict
from homeassistant.components.climate import FAN_OFF as FAN_OFF, HVACMode as HVACMode
from homeassistant.components.number import NumberMode as NumberMode
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA
from homeassistant.components.text import TextMode as TextMode
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_PAYLOAD as CONF_PAYLOAD, CONF_TYPE as CONF_TYPE, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, Platform as Platform
from homeassistant.helpers.entity import ENTITY_CATEGORIES_SCHEMA as ENTITY_CATEGORIES_SCHEMA
from typing import ClassVar, Final

def number_limit_sub_validator(entity_config: OrderedDict) -> OrderedDict: ...
def _max_payload_value(payload_length: int) -> int: ...
def button_payload_sub_validator(entity_config: OrderedDict) -> OrderedDict: ...
def select_options_sub_validator(entity_config: OrderedDict) -> OrderedDict: ...

class EventSchema:
    KNX_EVENT_FILTER_SCHEMA: Incomplete
    SCHEMA: Incomplete

class KNXPlatformSchema(ABC):
    PLATFORM: ClassVar[Platform | str]
    ENTITY_SCHEMA: ClassVar[vol.Schema | vol.All | vol.Any]
    @classmethod
    def platform_node(cls) -> dict[vol.Optional, vol.All]: ...

class BinarySensorSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_STATE_ADDRESS = CONF_STATE_ADDRESS
    CONF_SYNC_STATE = CONF_SYNC_STATE
    CONF_INVERT = CONF_INVERT
    CONF_IGNORE_INTERNAL_STATE: str
    CONF_CONTEXT_TIMEOUT: str
    CONF_RESET_AFTER = CONF_RESET_AFTER
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class ButtonSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_VALUE: str
    DEFAULT_NAME: str
    payload_or_value_msg: Incomplete
    length_or_type_msg: Incomplete
    ENTITY_SCHEMA: Incomplete

class ClimateSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_ACTIVE_STATE_ADDRESS: str
    CONF_SETPOINT_SHIFT_ADDRESS: str
    CONF_SETPOINT_SHIFT_STATE_ADDRESS: str
    CONF_SETPOINT_SHIFT_MODE: str
    CONF_SETPOINT_SHIFT_MAX: str
    CONF_SETPOINT_SHIFT_MIN: str
    CONF_TEMPERATURE_ADDRESS: str
    CONF_TEMPERATURE_STEP: str
    CONF_TARGET_TEMPERATURE_ADDRESS: str
    CONF_TARGET_TEMPERATURE_STATE_ADDRESS: str
    CONF_OPERATION_MODE_ADDRESS: str
    CONF_OPERATION_MODE_STATE_ADDRESS: str
    CONF_CONTROLLER_STATUS_ADDRESS: str
    CONF_CONTROLLER_STATUS_STATE_ADDRESS: str
    CONF_CONTROLLER_MODE_ADDRESS: str
    CONF_CONTROLLER_MODE_STATE_ADDRESS: str
    CONF_COMMAND_VALUE_STATE_ADDRESS: str
    CONF_HEAT_COOL_ADDRESS: str
    CONF_HEAT_COOL_STATE_ADDRESS: str
    CONF_OPERATION_MODE_FROST_PROTECTION_ADDRESS: str
    CONF_OPERATION_MODE_NIGHT_ADDRESS: str
    CONF_OPERATION_MODE_COMFORT_ADDRESS: str
    CONF_OPERATION_MODE_STANDBY_ADDRESS: str
    CONF_OPERATION_MODES: str
    CONF_CONTROLLER_MODES: str
    CONF_DEFAULT_CONTROLLER_MODE: str
    CONF_ON_OFF_ADDRESS: str
    CONF_ON_OFF_STATE_ADDRESS: str
    CONF_ON_OFF_INVERT: str
    CONF_MIN_TEMP: str
    CONF_MAX_TEMP: str
    CONF_FAN_SPEED_ADDRESS: str
    CONF_FAN_SPEED_STATE_ADDRESS: str
    CONF_FAN_MAX_STEP: str
    CONF_FAN_SPEED_MODE: str
    CONF_FAN_ZERO_MODE: str
    CONF_HUMIDITY_STATE_ADDRESS: str
    DEFAULT_NAME: str
    DEFAULT_SETPOINT_SHIFT_MODE: str
    DEFAULT_SETPOINT_SHIFT_MAX: int
    DEFAULT_SETPOINT_SHIFT_MIN: int
    DEFAULT_TEMPERATURE_STEP: float
    DEFAULT_ON_OFF_INVERT: bool
    DEFAULT_FAN_SPEED_MODE: str
    ENTITY_SCHEMA: Incomplete

class CoverSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_MOVE_LONG_ADDRESS: str
    CONF_MOVE_SHORT_ADDRESS: str
    CONF_STOP_ADDRESS: str
    CONF_POSITION_ADDRESS: str
    CONF_POSITION_STATE_ADDRESS: str
    CONF_ANGLE_ADDRESS: str
    CONF_ANGLE_STATE_ADDRESS: str
    CONF_TRAVELLING_TIME_DOWN: str
    CONF_TRAVELLING_TIME_UP: str
    CONF_INVERT_UPDOWN: str
    CONF_INVERT_POSITION: str
    CONF_INVERT_ANGLE: str
    DEFAULT_TRAVEL_TIME: int
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class DateSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class DateTimeSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class ExposeSchema(KNXPlatformSchema):
    PLATFORM = CONF_KNX_EXPOSE
    CONF_KNX_EXPOSE_TYPE = CONF_TYPE
    CONF_KNX_EXPOSE_ATTRIBUTE: str
    CONF_KNX_EXPOSE_BINARY: str
    CONF_KNX_EXPOSE_COOLDOWN: str
    CONF_KNX_EXPOSE_DEFAULT: str
    CONF_TIME: str
    CONF_DATE: str
    CONF_DATETIME: str
    EXPOSE_TIME_TYPES: Final[Incomplete]
    EXPOSE_TIME_SCHEMA: Incomplete
    EXPOSE_SENSOR_SCHEMA: Incomplete
    ENTITY_SCHEMA: Incomplete

class FanSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_STATE_ADDRESS = CONF_STATE_ADDRESS
    CONF_OSCILLATION_ADDRESS: str
    CONF_OSCILLATION_STATE_ADDRESS: str
    CONF_MAX_STEP: str
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class LightSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_STATE_ADDRESS = CONF_STATE_ADDRESS
    CONF_BRIGHTNESS_ADDRESS: str
    CONF_BRIGHTNESS_STATE_ADDRESS: str
    CONF_COLOR_ADDRESS: str
    CONF_COLOR_STATE_ADDRESS: str
    CONF_COLOR_TEMP_ADDRESS: str
    CONF_COLOR_TEMP_STATE_ADDRESS: str
    CONF_COLOR_TEMP_MODE: str
    CONF_HUE_ADDRESS: str
    CONF_HUE_STATE_ADDRESS: str
    CONF_RGBW_ADDRESS: str
    CONF_RGBW_STATE_ADDRESS: str
    CONF_SATURATION_ADDRESS: str
    CONF_SATURATION_STATE_ADDRESS: str
    CONF_XYY_ADDRESS: str
    CONF_XYY_STATE_ADDRESS: str
    CONF_MIN_KELVIN: str
    CONF_MAX_KELVIN: str
    DEFAULT_NAME: str
    DEFAULT_COLOR_TEMP_MODE: str
    DEFAULT_MIN_KELVIN: int
    DEFAULT_MAX_KELVIN: int
    CONF_INDIVIDUAL_COLORS: str
    CONF_RED: str
    CONF_GREEN: str
    CONF_BLUE: str
    CONF_WHITE: str
    _hs_color_inclusion_msg: str
    HS_COLOR_SCHEMA: Incomplete
    INDIVIDUAL_COLOR_SCHEMA: Incomplete
    ENTITY_SCHEMA: Incomplete

class NotifySchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class NumberSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_MAX: str
    CONF_MIN: str
    CONF_STEP: str
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class SceneSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_SCENE_NUMBER: str
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class SelectSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_OPTION: str
    CONF_OPTIONS: str
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class SensorSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_ALWAYS_CALLBACK: str
    CONF_STATE_ADDRESS = CONF_STATE_ADDRESS
    CONF_SYNC_STATE = CONF_SYNC_STATE
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class SwitchSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_INVERT = CONF_INVERT
    CONF_STATE_ADDRESS = CONF_STATE_ADDRESS
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class TextSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class TimeSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete

class WeatherSchema(KNXPlatformSchema):
    PLATFORM: Incomplete
    CONF_SYNC_STATE = CONF_SYNC_STATE
    CONF_KNX_TEMPERATURE_ADDRESS: str
    CONF_KNX_BRIGHTNESS_SOUTH_ADDRESS: str
    CONF_KNX_BRIGHTNESS_EAST_ADDRESS: str
    CONF_KNX_BRIGHTNESS_WEST_ADDRESS: str
    CONF_KNX_BRIGHTNESS_NORTH_ADDRESS: str
    CONF_KNX_WIND_SPEED_ADDRESS: str
    CONF_KNX_WIND_BEARING_ADDRESS: str
    CONF_KNX_RAIN_ALARM_ADDRESS: str
    CONF_KNX_FROST_ALARM_ADDRESS: str
    CONF_KNX_WIND_ALARM_ADDRESS: str
    CONF_KNX_DAY_NIGHT_ADDRESS: str
    CONF_KNX_AIR_PRESSURE_ADDRESS: str
    CONF_KNX_HUMIDITY_ADDRESS: str
    DEFAULT_NAME: str
    ENTITY_SCHEMA: Incomplete
