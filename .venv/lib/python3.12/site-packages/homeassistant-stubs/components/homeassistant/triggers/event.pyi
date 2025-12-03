from _typeshed import Incomplete
from homeassistant.const import CONF_EVENT_DATA as CONF_EVENT_DATA, CONF_PLATFORM as CONF_PLATFORM, EVENT_STATE_REPORTED as EVENT_STATE_REPORTED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import template as template
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONF_EVENT_TYPE: str
CONF_EVENT_CONTEXT: str

def _validate_event_types(value: Any) -> Any: ...

TRIGGER_SCHEMA: Incomplete

def _schema_value(value: Any) -> Any: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo, *, platform_type: str = 'event') -> CALLBACK_TYPE: ...
