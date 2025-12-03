import voluptuous as vol
from . import DOMAIN as DOMAIN
from .sensor import CONF_KEEP_LAST_SAMPLE as CONF_KEEP_LAST_SAMPLE, CONF_MAX_AGE as CONF_MAX_AGE, CONF_PERCENTILE as CONF_PERCENTILE, CONF_PRECISION as CONF_PRECISION, CONF_SAMPLES_MAX_BUFFER_SIZE as CONF_SAMPLES_MAX_BUFFER_SIZE, CONF_STATE_CHARACTERISTIC as CONF_STATE_CHARACTERISTIC, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PRECISION as DEFAULT_PRECISION, STATS_BINARY_SUPPORT as STATS_BINARY_SUPPORT, STATS_NUMERIC_SUPPORT as STATS_NUMERIC_SUPPORT, StatisticsSensor as StatisticsSensor
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, DurationSelector as DurationSelector, DurationSelectorConfig as DurationSelectorConfig, EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector
from typing import Any

async def get_state_characteristics(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def validate_options(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA_SETUP: Incomplete
DATA_SCHEMA_OPTIONS: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class StatisticsConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...

@websocket_api.async_response
async def ws_start_preview(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
