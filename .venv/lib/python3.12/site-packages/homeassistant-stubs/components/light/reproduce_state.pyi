from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ATTR_XY_COLOR as ATTR_XY_COLOR, _DEPRECATED_ATTR_COLOR_TEMP as _DEPRECATED_ATTR_COLOR_TEMP
from .const import ColorMode as ColorMode, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any, NamedTuple

_LOGGER: Incomplete
VALID_STATES: Incomplete
ATTR_GROUP: Incomplete
COLOR_GROUP: Incomplete

class ColorModeAttr(NamedTuple):
    parameter: str
    state_attr: str

COLOR_MODE_TO_ATTRIBUTE: Incomplete

def _color_mode_same(cur_state: State, state: State) -> bool: ...
async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
def check_attr_equal(attr1: Mapping, attr2: Mapping, attr_str: str) -> bool: ...
