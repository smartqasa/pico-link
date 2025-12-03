from .const import ATTR_DISPLAY_NAME as ATTR_DISPLAY_NAME, ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, EVENT_HOMEKIT_CHANGED as EVENT_HOMEKIT_CHANGED
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_ENTITY_ID as LOGBOOK_ENTRY_ENTITY_ID, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SERVICE as ATTR_SERVICE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event], dict[str, Any]]], None]) -> None: ...
