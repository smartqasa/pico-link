from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant import exceptions as exceptions
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_BELOW as CONF_BELOW, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HassJob as HassJob, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import condition as condition, template as template
from homeassistant.helpers.event import async_track_same_state as async_track_same_state, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

def validate_above_below[_T: dict[str, Any]](value: _T) -> _T: ...

_TRIGGER_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo, *, platform_type: str = 'numeric_state') -> CALLBACK_TYPE: ...
