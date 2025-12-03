from ..const import DOMAIN as DOMAIN
from ..helpers import async_get_device_entry_by_device_id as async_get_device_entry_by_device_id, async_get_device_id_from_entity_id as async_get_device_id_from_entity_id
from _typeshed import Incomplete
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.trigger import PluggableAction as PluggableAction, TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORM_TYPE: Incomplete
TRIGGER_TYPE_TURN_ON: str
TRIGGER_SCHEMA: Incomplete

def async_get_turn_on_trigger(device_id: str) -> dict[str, str]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo, *, platform_type: str = ...) -> CALLBACK_TYPE | None: ...
