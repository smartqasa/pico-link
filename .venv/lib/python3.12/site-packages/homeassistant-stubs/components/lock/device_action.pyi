from . import DOMAIN as DOMAIN, LockEntityFeature as LockEntityFeature
from _typeshed import Incomplete
from homeassistant.components.device_automation import async_validate_entity_schema as async_validate_entity_schema
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, SERVICE_LOCK as SERVICE_LOCK, SERVICE_OPEN as SERVICE_OPEN, SERVICE_UNLOCK as SERVICE_UNLOCK
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

ACTION_TYPES: Incomplete
_ACTION_SCHEMA: Incomplete

async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
