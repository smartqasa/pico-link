from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_SOURCE as CONF_SOURCE, CONF_ZONE as CONF_ZONE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HassJob as HassJob, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import entity_domain as entity_domain
from homeassistant.helpers.event import TrackStates as TrackStates, async_track_state_change_filtered as async_track_state_change_filtered
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_LOGGER: Incomplete
EVENT_ENTER: Final[str]
EVENT_LEAVE: Final[str]
DEFAULT_EVENT: Final[Incomplete]
TRIGGER_SCHEMA: Incomplete

def source_match(state: State | None, source: str) -> bool: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
