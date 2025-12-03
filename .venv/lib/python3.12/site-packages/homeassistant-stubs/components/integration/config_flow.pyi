import voluptuous as vol
from .const import CONF_MAX_SUB_INTERVAL as CONF_MAX_SUB_INTERVAL, CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_SOURCE_SENSOR as CONF_SOURCE_SENSOR, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, DOMAIN as DOMAIN, METHOD_LEFT as METHOD_LEFT, METHOD_RIGHT as METHOD_RIGHT, METHOD_TRAPEZOIDAL as METHOD_TRAPEZOIDAL
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, UnitOfTime as UnitOfTime
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from typing import Any

UNIT_PREFIXES: Incomplete
TIME_UNITS: Incomplete
INTEGRATION_METHODS: Incomplete
ALLOWED_DOMAINS: Incomplete

@callback
def entity_selector_compatible(handler: SchemaOptionsFlowHandler) -> selector.EntitySelector: ...
async def _get_options_dict(handler: SchemaCommonFlowHandler | None) -> dict: ...
async def _get_options_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def _get_config_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...

CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
