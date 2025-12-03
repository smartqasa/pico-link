from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_COMMAND_CLASS_NAME as ATTR_COMMAND_CLASS_NAME, ATTR_DATA_TYPE as ATTR_DATA_TYPE, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_EVENT_LABEL as ATTR_EVENT_LABEL, ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, ATTR_LABEL as ATTR_LABEL, ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, ZWAVE_JS_NOTIFICATION_EVENT as ZWAVE_JS_NOTIFICATION_EVENT, ZWAVE_JS_VALUE_NOTIFICATION_EVENT as ZWAVE_JS_VALUE_NOTIFICATION_EVENT
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event], dict[str, str]]], None]) -> None: ...
