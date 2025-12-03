from .const import CONF_AUTHOR as CONF_AUTHOR, CONF_BLUEPRINT as CONF_BLUEPRINT, CONF_COLLAPSED as CONF_COLLAPSED, CONF_HOMEASSISTANT as CONF_HOMEASSISTANT, CONF_INPUT as CONF_INPUT, CONF_MIN_VERSION as CONF_MIN_VERSION, CONF_SOURCE_URL as CONF_SOURCE_URL, CONF_USE_BLUEPRINT as CONF_USE_BLUEPRINT
from _typeshed import Incomplete
from homeassistant.const import CONF_DEFAULT as CONF_DEFAULT, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_DOMAIN as CONF_DOMAIN, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_PATH as CONF_PATH, CONF_SELECTOR as CONF_SELECTOR
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from typing import Any

def version_validator(value: Any) -> str: ...
def unique_input_validator(inputs: Any) -> Any: ...
@callback
def is_blueprint_config(config: Any) -> bool: ...
@callback
def is_blueprint_instance_config(config: Any) -> bool: ...

BLUEPRINT_INPUT_SCHEMA: Incomplete
BLUEPRINT_INPUT_SECTION_SCHEMA: Incomplete
BLUEPRINT_SCHEMA: Incomplete

def validate_yaml_suffix(value: str) -> str: ...

BLUEPRINT_INSTANCE_FIELDS: Incomplete
