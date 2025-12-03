import voluptuous as vol
from . import ATTR_CODE_ARM_REQUIRED as ATTR_CODE_ARM_REQUIRED, DOMAIN as DOMAIN
from .const import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature
from _typeshed import Incomplete
from homeassistant.components.device_automation import async_validate_entity_schema as async_validate_entity_schema
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CODE as CONF_CODE, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, SERVICE_ALARM_ARM_AWAY as SERVICE_ALARM_ARM_AWAY, SERVICE_ALARM_ARM_HOME as SERVICE_ALARM_ARM_HOME, SERVICE_ALARM_ARM_NIGHT as SERVICE_ALARM_ARM_NIGHT, SERVICE_ALARM_ARM_VACATION as SERVICE_ALARM_ARM_VACATION, SERVICE_ALARM_DISARM as SERVICE_ALARM_DISARM, SERVICE_ALARM_TRIGGER as SERVICE_ALARM_TRIGGER
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Final

ACTION_TYPES: Final[set[str]]
_ACTION_SCHEMA: Final[Incomplete]

async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
