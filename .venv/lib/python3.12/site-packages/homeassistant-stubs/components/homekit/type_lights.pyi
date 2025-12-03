from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_BRIGHTNESS as CHAR_BRIGHTNESS, CHAR_COLOR_TEMPERATURE as CHAR_COLOR_TEMPERATURE, CHAR_HUE as CHAR_HUE, CHAR_ON as CHAR_ON, CHAR_SATURATION as CHAR_SATURATION, PROP_MAX_VALUE as PROP_MAX_VALUE, PROP_MIN_VALUE as PROP_MIN_VALUE, SERV_LIGHTBULB as SERV_LIGHTBULB
from .util import get_min_max as get_min_max
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_MAX_COLOR_TEMP_KELVIN as ATTR_MAX_COLOR_TEMP_KELVIN, ATTR_MIN_COLOR_TEMP_KELVIN as ATTR_MIN_COLOR_TEMP_KELVIN, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES, ATTR_WHITE as ATTR_WHITE, ColorMode as ColorMode, brightness_supported as brightness_supported, color_supported as color_supported, color_temp_supported as color_temp_supported
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, State as State, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin, color_temperature_to_hs as color_temperature_to_hs, color_temperature_to_rgbww as color_temperature_to_rgbww
from typing import Any

_LOGGER: Incomplete
CHANGE_COALESCE_TIME_WINDOW: float
DEFAULT_MIN_COLOR_TEMP: int
DEFAULT_MAX_COLOR_TEMP: int
COLOR_MODES_WITH_WHITES: Incomplete

class Light(HomeAccessory):
    chars: Incomplete
    _event_timer: CALLBACK_TYPE | None
    _pending_events: dict[str, Any]
    color_modes: Incomplete
    _previous_color_mode: Incomplete
    color_supported: Incomplete
    color_temp_supported: Incomplete
    rgbw_supported: Incomplete
    rgbww_supported: Incomplete
    white_supported: Incomplete
    brightness_supported: Incomplete
    char_on: Incomplete
    char_brightness: Incomplete
    max_mireds: Incomplete
    char_color_temp: Incomplete
    char_hue: Incomplete
    char_saturation: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def _set_chars(self, char_values: dict[str, Any]) -> None: ...
    @callback
    def _async_send_events(self, _now: datetime) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...
