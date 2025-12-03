from .const import CONF_INVERT as CONF_INVERT, CONF_TARGET_DOMAIN as CONF_TARGET_DOMAIN, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, Platform as Platform
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, wrapped_entity_config_entry_title as wrapped_entity_config_entry_title
from typing import Any

TARGET_DOMAIN_OPTIONS: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class SwitchAsXConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    VERSION: int
    MINOR_VERSION: int
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
