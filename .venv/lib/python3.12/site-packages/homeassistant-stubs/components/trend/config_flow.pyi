import voluptuous as vol
from .const import CONF_INVERT as CONF_INVERT, CONF_MAX_SAMPLES as CONF_MAX_SAMPLES, CONF_MIN_GRADIENT as CONF_MIN_GRADIENT, CONF_MIN_SAMPLES as CONF_MIN_SAMPLES, CONF_SAMPLE_DURATION as CONF_SAMPLE_DURATION, DEFAULT_MAX_SAMPLES as DEFAULT_MAX_SAMPLES, DEFAULT_MIN_GRADIENT as DEFAULT_MIN_GRADIENT, DEFAULT_MIN_SAMPLES as DEFAULT_MIN_SAMPLES, DEFAULT_SAMPLE_DURATION as DEFAULT_SAMPLE_DURATION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, UnitOfTime as UnitOfTime
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from typing import Any

async def get_base_options_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def get_extended_options_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...

CONFIG_SCHEMA: Incomplete

class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow: Incomplete
    options_flow: Incomplete
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
