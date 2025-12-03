from .const import DOMAIN as DOMAIN, EVENT_TURN_ON as EVENT_TURN_ON
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

TRIGGER_TYPES: Incomplete
TRIGGER_SCHEMA: Incomplete

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
