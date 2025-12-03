from .const import DEVICE_ID as DEVICE_ID, DOMAIN as DOMAIN, EVENT_TAG_SCANNED as EVENT_TAG_SCANNED, TAG_ID as TAG_ID
from _typeshed import Incomplete
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
