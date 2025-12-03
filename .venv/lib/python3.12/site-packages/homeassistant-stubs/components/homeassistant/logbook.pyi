from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_ICON as LOGBOOK_ENTRY_ICON, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import NoEventData as NoEventData
from homeassistant.util.event_type import EventType as EventType
from typing import Any

EVENT_TO_NAME: dict[EventType[Any] | str, str]

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, EventType[NoEventData] | str, Callable[[Event], dict[str, str]]], None]) -> None: ...
