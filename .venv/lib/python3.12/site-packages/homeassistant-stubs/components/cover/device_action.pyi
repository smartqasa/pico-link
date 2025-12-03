import voluptuous as vol
from . import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntityFeature as CoverEntityFeature, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_automation import async_validate_entity_schema as async_validate_entity_schema
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

CMD_ACTION_TYPES: Incomplete
POSITION_ACTION_TYPES: Incomplete
CMD_ACTION_SCHEMA: Incomplete
POSITION_ACTION_SCHEMA: Incomplete
_ACTION_SCHEMA: Incomplete

async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
