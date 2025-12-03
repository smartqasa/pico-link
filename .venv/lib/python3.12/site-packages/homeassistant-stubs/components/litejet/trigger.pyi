from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import track_point_in_utc_time as track_point_in_utc_time
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from pylitejet import LiteJet as LiteJet

CONF_NUMBER: str
CONF_HELD_MORE_THAN: str
CONF_HELD_LESS_THAN: str
TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
