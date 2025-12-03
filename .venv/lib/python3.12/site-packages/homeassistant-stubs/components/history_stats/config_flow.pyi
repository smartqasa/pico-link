from .const import CONF_DURATION as CONF_DURATION, CONF_END as CONF_END, CONF_PERIOD_KEYS as CONF_PERIOD_KEYS, CONF_START as CONF_START, CONF_TYPE_KEYS as CONF_TYPE_KEYS, CONF_TYPE_TIME as CONF_TYPE_TIME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_STATE as CONF_STATE, CONF_TYPE as CONF_TYPE
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import DurationSelector as DurationSelector, DurationSelectorConfig as DurationSelectorConfig, EntitySelector as EntitySelector, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig
from typing import Any

async def validate_options(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA_SETUP: Incomplete
DATA_SCHEMA_OPTIONS: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class StatisticsConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
