from . import get_entity_ids as get_entity_ids
from collections.abc import Iterable
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.state import async_reproduce_state as async_reproduce_state
from typing import Any

async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
