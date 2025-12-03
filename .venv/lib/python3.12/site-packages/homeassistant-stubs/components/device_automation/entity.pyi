import voluptuous as vol
from . import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from .const import CONF_CHANGED_STATES as CONF_CHANGED_STATES
from _typeshed import Incomplete
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

ENTITY_TRIGGERS: Incomplete
TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
async def _async_get_automations(hass: HomeAssistant, device_id: str, automation_templates: list[dict[str, str]], domain: str) -> list[dict[str, str]]: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str, domain: str) -> list[dict[str, str]]: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
