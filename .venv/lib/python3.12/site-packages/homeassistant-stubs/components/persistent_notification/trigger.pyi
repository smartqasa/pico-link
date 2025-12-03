from . import Notification as Notification, UpdateType as UpdateType, async_register_callback as async_register_callback
from _typeshed import Incomplete
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerData as TriggerData, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_LOGGER: Incomplete
CONF_NOTIFICATION_ID: Final[str]
CONF_UPDATE_TYPE: Final[str]
TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
