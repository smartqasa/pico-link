from .const import ATTR_HUMIDITY as ATTR_HUMIDITY, DOMAIN as DOMAIN, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_MODE as SERVICE_SET_MODE
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.const import ATTR_MODE as ATTR_MODE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

_LOGGER: Incomplete

async def _async_reproduce_states(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
