import voluptuous as vol
from .const import DOMAIN as DOMAIN, KEY_ACTIONS as KEY_ACTIONS, SENDKEYS as SENDKEYS
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.homeassistant.triggers import event as event
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

TRIGGER_TYPES: Incomplete
LCN_DEVICE_TRIGGER_BASE_SCHEMA: Incomplete
ACCESS_CONTROL_SCHEMA: Incomplete
TRANSMITTER_SCHEMA: Incomplete
SENDKEYS_SCHEMA: Incomplete
TRIGGER_SCHEMA: Incomplete
TYPE_SCHEMAS: Incomplete

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
