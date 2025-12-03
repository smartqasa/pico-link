from ..config_validation import VALUE_SCHEMA as VALUE_SCHEMA
from ..const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_COMMAND_CLASS_NAME as ATTR_COMMAND_CLASS_NAME, ATTR_CURRENT_VALUE as ATTR_CURRENT_VALUE, ATTR_CURRENT_VALUE_RAW as ATTR_CURRENT_VALUE_RAW, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_NODE_ID as ATTR_NODE_ID, ATTR_PREVIOUS_VALUE as ATTR_PREVIOUS_VALUE, ATTR_PREVIOUS_VALUE_RAW as ATTR_PREVIOUS_VALUE_RAW, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_PROPERTY_KEY_NAME as ATTR_PROPERTY_KEY_NAME, ATTR_PROPERTY_NAME as ATTR_PROPERTY_NAME, DOMAIN as DOMAIN, EVENT_VALUE_UPDATED as EVENT_VALUE_UPDATED
from ..helpers import async_get_nodes_from_targets as async_get_nodes_from_targets, get_device_id as get_device_id
from .trigger_helpers import async_bypass_dynamic_config_validation as async_bypass_dynamic_config_validation
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM, MATCH_ALL as MATCH_ALL
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as Value

PLATFORM_TYPE: Incomplete
ATTR_FROM: str
ATTR_TO: str
TRIGGER_SCHEMA: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo, *, platform_type: str = ...) -> CALLBACK_TYPE: ...
