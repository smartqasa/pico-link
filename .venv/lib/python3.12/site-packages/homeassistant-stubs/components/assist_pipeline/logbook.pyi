from .const import DOMAIN as DOMAIN, EVENT_RECORDING as EVENT_RECORDING
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event], dict[str, str]]], None]) -> None: ...
