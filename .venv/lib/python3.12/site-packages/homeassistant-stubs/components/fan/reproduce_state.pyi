from . import ATTR_DIRECTION as ATTR_DIRECTION, ATTR_OSCILLATING as ATTR_OSCILLATING, ATTR_PERCENTAGE as ATTR_PERCENTAGE, ATTR_PRESET_MODE as ATTR_PRESET_MODE, DOMAIN as DOMAIN, SERVICE_OSCILLATE as SERVICE_OSCILLATE, SERVICE_SET_DIRECTION as SERVICE_SET_DIRECTION, SERVICE_SET_PERCENTAGE as SERVICE_SET_PERCENTAGE, SERVICE_SET_PRESET_MODE as SERVICE_SET_PRESET_MODE
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

_LOGGER: Incomplete
VALID_STATES: Incomplete
SPEED_AND_MODE_ATTRIBUTES: Incomplete
SIMPLE_ATTRIBUTES: Incomplete

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
