from .const import CONF_AC_MODE as CONF_AC_MODE, CONF_COLD_TOLERANCE as CONF_COLD_TOLERANCE, CONF_HEATER as CONF_HEATER, CONF_HOT_TOLERANCE as CONF_HOT_TOLERANCE, CONF_MAX_TEMP as CONF_MAX_TEMP, CONF_MIN_DUR as CONF_MIN_DUR, CONF_MIN_TEMP as CONF_MIN_TEMP, CONF_PRESETS as CONF_PRESETS, CONF_SENSOR as CONF_SENSOR, DEFAULT_TOLERANCE as DEFAULT_TOLERANCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import fan as fan, switch as switch
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CONF_NAME as CONF_NAME, DEGREE as DEGREE
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from typing import Any

OPTIONS_SCHEMA: Incomplete
PRESETS_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
