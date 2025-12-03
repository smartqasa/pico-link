from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import sensor as sensor
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, CONF_AT as CONF_AT, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_OFFSET as CONF_OFFSET, CONF_PLATFORM as CONF_PLATFORM, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HassJob as HassJob, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import template as template
from homeassistant.helpers.event import async_track_point_in_time as async_track_point_in_time, async_track_state_change_event as async_track_state_change_event, async_track_time_change as async_track_time_change
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, NamedTuple

_TIME_TRIGGER_ENTITY: Incomplete
_TIME_AT_SCHEMA: Incomplete
_TIME_TRIGGER_ENTITY_WITH_OFFSET: Incomplete

def valid_at_template(value: Any) -> template.Template: ...

_TIME_TRIGGER_SCHEMA: Incomplete
TRIGGER_SCHEMA: Incomplete

class TrackEntity(NamedTuple):
    entity_id: str
    callback: Callable

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
