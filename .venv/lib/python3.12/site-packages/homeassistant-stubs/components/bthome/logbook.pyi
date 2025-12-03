from .const import BTHOME_BLE_EVENT as BTHOME_BLE_EVENT, BTHomeBleEvent as BTHomeBleEvent, DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event[BTHomeBleEvent]], dict[str, str]]], None]) -> None: ...
