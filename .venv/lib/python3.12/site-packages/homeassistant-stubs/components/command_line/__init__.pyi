from .const import CONF_COMMAND_TIMEOUT as CONF_COMMAND_TIMEOUT, CONF_JSON_ATTRIBUTES as CONF_JSON_ATTRIBUTES, CONF_JSON_ATTRIBUTES_PATH as CONF_JSON_ATTRIBUTES_PATH, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS
from homeassistant.const import CONF_COMMAND as CONF_COMMAND, CONF_COMMAND_CLOSE as CONF_COMMAND_CLOSE, CONF_COMMAND_OFF as CONF_COMMAND_OFF, CONF_COMMAND_ON as CONF_COMMAND_ON, CONF_COMMAND_OPEN as CONF_COMMAND_OPEN, CONF_COMMAND_STATE as CONF_COMMAND_STATE, CONF_COMMAND_STOP as CONF_COMMAND_STOP, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, Platform as Platform, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.entity_platform import async_get_platforms as async_get_platforms
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

BINARY_SENSOR_DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
SENSOR_DEFAULT_NAME: str
CONF_NOTIFIERS: str
PLATFORM_MAPPING: Incomplete
_LOGGER: Incomplete
BINARY_SENSOR_SCHEMA: Incomplete
COVER_SCHEMA: Incomplete
NOTIFY_SCHEMA: Incomplete
SENSOR_SCHEMA: Incomplete
SWITCH_SCHEMA: Incomplete
COMBINED_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_load_platforms(hass: HomeAssistant, command_line_config: list[dict[str, dict[str, Any]]], config: ConfigType) -> None: ...
