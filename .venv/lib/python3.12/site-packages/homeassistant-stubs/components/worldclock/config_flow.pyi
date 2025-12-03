import voluptuous as vol
from .const import CONF_TIME_FORMAT as CONF_TIME_FORMAT, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_TIME_STR_FORMAT as DEFAULT_TIME_STR_FORMAT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TIME_ZONE as CONF_TIME_ZONE
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector
from typing import Any

TIME_STR_OPTIONS: Incomplete

async def validate_duplicate(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def get_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...

DATA_SCHEMA_OPTIONS: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class WorldclockConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
