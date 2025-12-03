from .const import CONF_ADVANCED as CONF_ADVANCED, CONF_EXAMPLE as CONF_EXAMPLE, CONF_FIELDS as CONF_FIELDS, CONF_REQUIRED as CONF_REQUIRED, CONF_TRACE as CONF_TRACE, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import async_get_blueprints as async_get_blueprints
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.blueprint import BlueprintException as BlueprintException, is_blueprint_instance_config as is_blueprint_instance_config
from homeassistant.components.trace import TRACE_CONFIG_SCHEMA as TRACE_CONFIG_SCHEMA
from homeassistant.config import config_per_platform as config_per_platform, config_without_domain as config_without_domain
from homeassistant.const import CONF_ALIAS as CONF_ALIAS, CONF_DEFAULT as CONF_DEFAULT, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_SELECTOR as CONF_SELECTOR, CONF_SEQUENCE as CONF_SEQUENCE, CONF_VARIABLES as CONF_VARIABLES, SERVICE_RELOAD as SERVICE_RELOAD, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.script import SCRIPT_MODE_SINGLE as SCRIPT_MODE_SINGLE, async_validate_actions_config as async_validate_actions_config, make_script_schema as make_script_schema
from homeassistant.helpers.selector import validate_selector as validate_selector
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.yaml.input import UndefinedSubstitution as UndefinedSubstitution
from typing import Any

PACKAGE_MERGE_HINT: str
_MINIMAL_SCRIPT_ENTITY_SCHEMA: Incomplete
_INVALID_OBJECT_IDS: Incomplete
_SCRIPT_OBJECT_ID_SCHEMA: Incomplete
SCRIPT_ENTITY_SCHEMA: Incomplete

async def _async_validate_config_item(hass: HomeAssistant, object_id: str, config: ConfigType, raise_on_errors: bool, warn_on_errors: bool) -> ScriptConfig: ...

class ValidationStatus(StrEnum):
    FAILED_BLUEPRINT = 'failed_blueprint'
    FAILED_SCHEMA = 'failed_schema'
    FAILED_SEQUENCE = 'failed_sequence'
    OK = 'ok'

class ScriptConfig(dict):
    raw_config: ConfigType | None
    raw_blueprint_inputs: ConfigType | None
    validation_status: ValidationStatus
    validation_error: str | None

async def _try_async_validate_config_item(hass: HomeAssistant, object_id: str, config: ConfigType) -> ScriptConfig | None: ...
async def async_validate_config_item(hass: HomeAssistant, object_id: str, config: dict[str, Any]) -> ScriptConfig | None: ...
async def async_validate_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
