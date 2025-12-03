from .const import CONF_CALIBRATION_FACTOR as CONF_CALIBRATION_FACTOR, CONF_INDOOR_HUMIDITY as CONF_INDOOR_HUMIDITY, CONF_INDOOR_TEMP as CONF_INDOOR_TEMP, CONF_OUTDOOR_TEMP as CONF_OUTDOOR_TEMP, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .sensor import MoldIndicator as MoldIndicator
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, TextSelector as TextSelector
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

async def validate_input(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA_OPTIONS: Incomplete
DATA_SCHEMA_CONFIG: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class MoldIndicatorConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...

@callback
def ws_start_preview(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
