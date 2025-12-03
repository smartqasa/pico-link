from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_automation import async_validate_entity_schema as async_validate_entity_schema, toggle_entity as toggle_entity
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

_ACTION_SCHEMA: Incomplete

async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
