from ..const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

EVENT_START: str
EVENT_SHUTDOWN: str
TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
