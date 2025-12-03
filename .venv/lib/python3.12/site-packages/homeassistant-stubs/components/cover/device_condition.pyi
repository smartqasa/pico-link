import voluptuous as vol
from . import CoverEntityFeature as CoverEntityFeature, CoverState as CoverState, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

POSITION_CONDITION_TYPES: Incomplete
STATE_CONDITION_TYPES: Incomplete
POSITION_CONDITION_SCHEMA: Incomplete
STATE_CONDITION_SCHEMA: Incomplete
CONDITION_SCHEMA: Incomplete

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
@callback
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
