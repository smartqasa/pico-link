from . import ATTR_OPTIONS as ATTR_OPTIONS, DOMAIN as DOMAIN, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION, SERVICE_SET_OPTIONS as SERVICE_SET_OPTIONS
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_OPTION as ATTR_OPTION
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

ATTR_GROUP: Incomplete
_LOGGER: Incomplete

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
def check_attr_equal(attr1: Mapping, attr2: Mapping, attr_str: str) -> bool: ...
