import voluptuous as vol
from .config_validation import VALUE_SCHEMA as VALUE_SCHEMA
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_CONFIG_PARAMETER as ATTR_CONFIG_PARAMETER, ATTR_CONFIG_PARAMETER_BITMASK as ATTR_CONFIG_PARAMETER_BITMASK, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_METER_TYPE as ATTR_METER_TYPE, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_REFRESH_ALL_VALUES as ATTR_REFRESH_ALL_VALUES, ATTR_VALUE as ATTR_VALUE, ATTR_WAIT_FOR_RESULT as ATTR_WAIT_FOR_RESULT, DOMAIN as DOMAIN, SERVICE_CLEAR_LOCK_USERCODE as SERVICE_CLEAR_LOCK_USERCODE, SERVICE_PING as SERVICE_PING, SERVICE_REFRESH_VALUE as SERVICE_REFRESH_VALUE, SERVICE_RESET_METER as SERVICE_RESET_METER, SERVICE_SET_CONFIG_PARAMETER as SERVICE_SET_CONFIG_PARAMETER, SERVICE_SET_LOCK_USERCODE as SERVICE_SET_LOCK_USERCODE, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from .device_automation_helpers import CONF_SUBTYPE as CONF_SUBTYPE, VALUE_ID_REGEX as VALUE_ID_REGEX, generate_config_parameter_subtype as generate_config_parameter_subtype
from .helpers import async_get_node_from_device_id as async_get_node_from_device_id, get_value_state_schema as get_value_state_schema
from _typeshed import Incomplete
from homeassistant.components.device_automation import async_validate_entity_schema as async_validate_entity_schema
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_DOMAIN as ATTR_DOMAIN, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

ACTION_TYPES: Incomplete
CLEAR_LOCK_USERCODE_SCHEMA: Incomplete
PING_SCHEMA: Incomplete
REFRESH_VALUE_SCHEMA: Incomplete
RESET_METER_SCHEMA: Incomplete
SET_CONFIG_PARAMETER_SCHEMA: Incomplete
SET_LOCK_USERCODE_SCHEMA: Incomplete
SET_VALUE_SCHEMA: Incomplete
_ACTION_SCHEMA: Incomplete

async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
