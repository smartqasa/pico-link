from .binary_sensor import ThresholdSensor as ThresholdSensor
from .const import CONF_HYSTERESIS as CONF_HYSTERESIS, CONF_LOWER as CONF_LOWER, CONF_UPPER as CONF_UPPER, DEFAULT_HYSTERESIS as DEFAULT_HYSTERESIS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep
from typing import Any

async def _validate_mode(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

OPTIONS_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...

@callback
def ws_start_preview(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
