from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_ACTIVE as CHAR_ACTIVE, CHAR_NAME as CHAR_NAME, CHAR_ON as CHAR_ON, CHAR_ROTATION_DIRECTION as CHAR_ROTATION_DIRECTION, CHAR_ROTATION_SPEED as CHAR_ROTATION_SPEED, CHAR_SWING_MODE as CHAR_SWING_MODE, CHAR_TARGET_FAN_STATE as CHAR_TARGET_FAN_STATE, PROP_MIN_STEP as PROP_MIN_STEP, SERV_FANV2 as SERV_FANV2, SERV_SWITCH as SERV_SWITCH
from .util import cleanup_name_for_homekit as cleanup_name_for_homekit
from _typeshed import Incomplete
from homeassistant.components.fan import ATTR_DIRECTION as ATTR_DIRECTION, ATTR_OSCILLATING as ATTR_OSCILLATING, ATTR_PERCENTAGE as ATTR_PERCENTAGE, ATTR_PERCENTAGE_STEP as ATTR_PERCENTAGE_STEP, ATTR_PRESET_MODE as ATTR_PRESET_MODE, ATTR_PRESET_MODES as ATTR_PRESET_MODES, DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntityFeature as FanEntityFeature, SERVICE_OSCILLATE as SERVICE_OSCILLATE, SERVICE_SET_DIRECTION as SERVICE_SET_DIRECTION, SERVICE_SET_PERCENTAGE as SERVICE_SET_PERCENTAGE, SERVICE_SET_PRESET_MODE as SERVICE_SET_PRESET_MODE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import State as State, callback as callback
from typing import Any

_LOGGER: Incomplete

class Fan(HomeAccessory):
    chars: list[str]
    preset_modes: list[str] | None
    char_active: Incomplete
    char_direction: Incomplete
    char_speed: Incomplete
    char_swing: Incomplete
    char_target_fan_state: Incomplete
    preset_mode_chars: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def _set_chars(self, char_values: dict[str, Any]) -> None: ...
    def set_single_preset_mode(self, value: int) -> None: ...
    def set_preset_mode(self, value: int, preset_mode: str) -> None: ...
    def set_state(self, value: int) -> None: ...
    def set_direction(self, value: int) -> None: ...
    def set_oscillating(self, value: int) -> None: ...
    def set_percentage(self, value: float) -> None: ...
    _state: Incomplete
    @callback
    def async_update_state(self, new_state: State) -> None: ...
