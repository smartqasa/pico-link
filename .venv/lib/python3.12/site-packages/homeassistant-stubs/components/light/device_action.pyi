import voluptuous as vol
from . import ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_BRIGHTNESS_STEP_PCT as ATTR_BRIGHTNESS_STEP_PCT, ATTR_FLASH as ATTR_FLASH, FLASH_SHORT as FLASH_SHORT, VALID_BRIGHTNESS_PCT as VALID_BRIGHTNESS_PCT, VALID_FLASH as VALID_FLASH, brightness_supported as brightness_supported, get_supported_color_modes as get_supported_color_modes
from .const import DOMAIN as DOMAIN, LightEntityFeature as LightEntityFeature
from _typeshed import Incomplete
from homeassistant.components.device_automation import async_get_entity_registry_entry_or_raise as async_get_entity_registry_entry_or_raise, async_validate_entity_schema as async_validate_entity_schema, toggle_entity as toggle_entity
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType, VolDictType as VolDictType

TYPE_BRIGHTNESS_INCREASE: str
TYPE_BRIGHTNESS_DECREASE: str
TYPE_FLASH: str
_ACTION_SCHEMA: Incomplete

async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
