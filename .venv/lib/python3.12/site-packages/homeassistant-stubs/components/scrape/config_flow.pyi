import voluptuous as vol
from . import COMBINED_SCHEMA as COMBINED_SCHEMA
from .const import CONF_ENCODING as CONF_ENCODING, CONF_INDEX as CONF_INDEX, CONF_SELECT as CONF_SELECT, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.rest import create_rest_data_from_config as create_rest_data_from_config
from homeassistant.components.rest.data import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from homeassistant.components.rest.schema import DEFAULT_METHOD as DEFAULT_METHOD, METHODS as METHODS
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HEADERS as CONF_HEADERS, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PAYLOAD as CONF_PAYLOAD, CONF_RESOURCE as CONF_RESOURCE, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_USERNAME as CONF_USERNAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import async_get_hass as async_get_hass
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, ObjectSelector as ObjectSelector, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY
from typing import Any

RESOURCE_SETUP: Incomplete
SENSOR_SETUP: Incomplete

async def validate_rest_setup(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_sensor_setup(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_select_sensor(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def get_select_sensor_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def get_edit_sensor_suggested_values(handler: SchemaCommonFlowHandler) -> dict[str, Any]: ...
async def validate_sensor_edit(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def get_remove_sensor_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def validate_remove_sensor(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA_RESOURCE: Incomplete
DATA_SCHEMA_EDIT_SENSOR: Incomplete
DATA_SCHEMA_SENSOR: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class ScrapeConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
