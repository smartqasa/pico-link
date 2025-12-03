from .const import ATTR_KEY as ATTR_KEY, ATTR_KEYPAD_ID as ATTR_KEYPAD_ID, ATTR_KEYPAD_NAME as ATTR_KEYPAD_NAME, ATTR_KEY_NAME as ATTR_KEY_NAME, DOMAIN as DOMAIN, EVENT_ELKM1_KEYPAD_KEY_PRESSED as EVENT_ELKM1_KEYPAD_KEY_PRESSED
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event], dict[str, str]]], None]) -> None: ...
