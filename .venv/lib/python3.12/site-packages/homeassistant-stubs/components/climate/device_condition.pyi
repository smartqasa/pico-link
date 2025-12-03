import voluptuous as vol
from . import DOMAIN as DOMAIN, const as const
from _typeshed import Incomplete
from homeassistant.components.device_automation import async_get_entity_registry_entry_or_raise as async_get_entity_registry_entry_or_raise
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.entity import get_capability as get_capability, get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

CONDITION_TYPES: Incomplete
HVAC_MODE_CONDITION: Incomplete
PRESET_MODE_CONDITION: Incomplete
CONDITION_SCHEMA: Incomplete

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
@callback
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
