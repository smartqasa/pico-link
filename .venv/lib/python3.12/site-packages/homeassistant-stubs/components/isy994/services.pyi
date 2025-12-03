from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from _typeshed import Incomplete
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_COMMAND as CONF_COMMAND, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import async_get_platforms as async_get_platforms
from homeassistant.helpers.service import entity_service_call as entity_service_call
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

SERVICE_SEND_PROGRAM_COMMAND: str
SERVICE_SEND_RAW_NODE_COMMAND: str
SERVICE_SEND_NODE_COMMAND: str
SERVICE_GET_ZWAVE_PARAMETER: str
SERVICE_SET_ZWAVE_PARAMETER: str
SERVICE_RENAME_NODE: str
SERVICE_SET_ZWAVE_LOCK_USER_CODE: str
SERVICE_DELETE_ZWAVE_LOCK_USER_CODE: str
CONF_PARAMETER: str
CONF_PARAMETERS: str
CONF_USER_NUM: str
CONF_CODE: str
CONF_VALUE: str
CONF_INIT: str
CONF_ISY: str
CONF_SIZE: str
VALID_NODE_COMMANDS: Incomplete
VALID_PROGRAM_COMMANDS: Incomplete
VALID_PARAMETER_SIZES: Incomplete

def valid_isy_commands(value: Any) -> str: ...

SCHEMA_GROUP: str
SERVICE_SEND_RAW_NODE_COMMAND_SCHEMA: Incomplete
SERVICE_SEND_NODE_COMMAND_SCHEMA: Incomplete
SERVICE_RENAME_NODE_SCHEMA: Incomplete
SERVICE_GET_ZWAVE_PARAMETER_SCHEMA: Incomplete
SERVICE_SET_ZWAVE_PARAMETER_SCHEMA: Incomplete
SERVICE_SET_USER_CODE_SCHEMA: VolDictType
SERVICE_DELETE_USER_CODE_SCHEMA: VolDictType
SERVICE_SEND_PROGRAM_COMMAND_SCHEMA: Incomplete

def async_get_entities(hass: HomeAssistant) -> dict[str, Entity]: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
@callback
def async_unload_services(hass: HomeAssistant) -> None: ...
