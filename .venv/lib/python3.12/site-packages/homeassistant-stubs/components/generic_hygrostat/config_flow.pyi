from . import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_DRY_TOLERANCE as CONF_DRY_TOLERANCE, CONF_HUMIDIFIER as CONF_HUMIDIFIER, CONF_MIN_DUR as CONF_MIN_DUR, CONF_SENSOR as CONF_SENSOR, CONF_WET_TOLERANCE as CONF_WET_TOLERANCE, DEFAULT_TOLERANCE as DEFAULT_TOLERANCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import fan as fan, switch as switch
from homeassistant.components.humidifier import HumidifierDeviceClass as HumidifierDeviceClass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CONF_NAME as CONF_NAME, PERCENTAGE as PERCENTAGE
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
