from .const import CONF_AFTER_TIME as CONF_AFTER_TIME, CONF_BEFORE_TIME as CONF_BEFORE_TIME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from typing import Any

OPTIONS_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
