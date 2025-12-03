from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.lock import LockState as LockState
from homeassistant.components.sun import STATE_ABOVE_HORIZON as STATE_ABOVE_HORIZON, STATE_BELOW_HORIZON as STATE_BELOW_HORIZON
from homeassistant.const import STATE_CLOSED as STATE_CLOSED, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_OPEN as STATE_OPEN, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration, bind_hass as bind_hass
from typing import Any

_LOGGER: Incomplete

@bind_hass
async def async_reproduce_state(hass: HomeAssistant, states: State | Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
def state_as_number(state: State) -> float: ...
