from _typeshed import Incomplete
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_ZONE as CONF_ZONE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition, location as location
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

EVENT_ENTER: str
EVENT_LEAVE: str
DEFAULT_EVENT = EVENT_ENTER
_LOGGER: Incomplete
_EVENT_DESCRIPTION: Incomplete
_TRIGGER_SCHEMA: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo, *, platform_type: str = 'zone') -> CALLBACK_TYPE: ...
