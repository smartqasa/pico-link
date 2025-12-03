import voluptuous as vol
from . import CoverEntityFeature as CoverEntityFeature, CoverState as CoverState, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

POSITION_TRIGGER_TYPES: Incomplete
STATE_TRIGGER_TYPES: Incomplete
POSITION_TRIGGER_SCHEMA: Incomplete
STATE_TRIGGER_SCHEMA: Incomplete
TRIGGER_SCHEMA: Incomplete

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
