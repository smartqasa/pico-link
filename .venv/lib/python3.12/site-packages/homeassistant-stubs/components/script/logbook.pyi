from . import DOMAIN as DOMAIN, EVENT_SCRIPT_STARTED as EVENT_SCRIPT_STARTED
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_CONTEXT_ID as LOGBOOK_ENTRY_CONTEXT_ID, LOGBOOK_ENTRY_ENTITY_ID as LOGBOOK_ENTRY_ENTITY_ID, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME, LazyEventPartialState as LazyEventPartialState
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[LazyEventPartialState], dict[str, Any]]], None]) -> None: ...
