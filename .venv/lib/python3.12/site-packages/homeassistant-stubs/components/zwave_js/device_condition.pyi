import voluptuous as vol
from .config_validation import VALUE_SCHEMA as VALUE_SCHEMA
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN
from .device_automation_helpers import CONF_SUBTYPE as CONF_SUBTYPE, CONF_VALUE_ID as CONF_VALUE_ID, NODE_STATUSES as NODE_STATUSES, async_bypass_dynamic_config_validation as async_bypass_dynamic_config_validation, generate_config_parameter_subtype as generate_config_parameter_subtype
from .helpers import async_get_node_from_device_id as async_get_node_from_device_id, check_type_schema_map as check_type_schema_map, get_value_state_schema as get_value_state_schema, get_zwave_value_from_config as get_zwave_value_from_config, remove_keys_with_empty_values as remove_keys_with_empty_values
from _typeshed import Incomplete
from homeassistant.components.device_automation import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import condition as condition
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

CONF_STATUS: str
NODE_STATUS_TYPE: str
CONFIG_PARAMETER_TYPE: str
VALUE_TYPE: str
CONDITION_TYPES: Incomplete
NODE_STATUS_CONDITION_SCHEMA: Incomplete
CONFIG_PARAMETER_CONDITION_SCHEMA: Incomplete
VALUE_CONDITION_SCHEMA: Incomplete
TYPE_SCHEMA_MAP: Incomplete
CONDITION_TYPE_SCHEMA: Incomplete
CONDITION_SCHEMA: Incomplete

async def async_validate_condition_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
@callback
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
