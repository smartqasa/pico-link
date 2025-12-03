from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_BROADCAST_ADDRESS as CONF_BROADCAST_ADDRESS, CONF_BROADCAST_PORT as CONF_BROADCAST_PORT, CONF_MAC as CONF_MAC
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, TextSelector as TextSelector
from typing import Any

async def validate(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_options(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class WakeonLanConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
