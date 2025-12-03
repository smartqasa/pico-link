from . import ATTR_DURATION as ATTR_DURATION, DOMAIN as DOMAIN, SERVICE_CANCEL as SERVICE_CANCEL, SERVICE_PAUSE as SERVICE_PAUSE, SERVICE_START as SERVICE_START, STATUS_ACTIVE as STATUS_ACTIVE, STATUS_IDLE as STATUS_IDLE, STATUS_PAUSED as STATUS_PAUSED
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

_LOGGER: Incomplete
VALID_STATES: Incomplete

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
