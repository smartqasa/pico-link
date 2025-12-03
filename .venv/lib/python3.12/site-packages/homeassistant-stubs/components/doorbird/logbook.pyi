from .const import DOMAIN as DOMAIN
from .util import async_get_entries as async_get_entries
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_ENTITY_ID as LOGBOOK_ENTRY_ENTITY_ID, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event], dict[str, str | None]]], None]) -> None: ...
