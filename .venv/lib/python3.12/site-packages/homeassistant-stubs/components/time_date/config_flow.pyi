from .const import CONF_DISPLAY_OPTIONS as CONF_DISPLAY_OPTIONS, DOMAIN as DOMAIN, OPTION_TYPES as OPTION_TYPES
from .sensor import TimeDateSensor as TimeDateSensor
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform
from typing import Any

_LOGGER: Incomplete
USER_SCHEMA: Incomplete

async def validate_input(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

CONFIG_FLOW: Incomplete

class TimeDateConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    def async_config_flow_finished(self, options: Mapping[str, Any]) -> None: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...

@websocket_api.async_response
async def ws_start_preview(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
