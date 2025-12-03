from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant import exceptions as exceptions
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, MATCH_ALL as MATCH_ALL
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HassJob as HassJob, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import template as template
from homeassistant.helpers.event import async_track_same_state as async_track_same_state, async_track_state_change_event as async_track_state_change_event, process_state_match as process_state_match
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONF_ENTITY_ID: str
CONF_FROM: str
CONF_TO: str
CONF_NOT_FROM: str
CONF_NOT_TO: str
BASE_SCHEMA: Incomplete
TRIGGER_STATE_SCHEMA: Incomplete
TRIGGER_ATTRIBUTE_SCHEMA: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo, *, platform_type: str = 'state') -> CALLBACK_TYPE: ...
