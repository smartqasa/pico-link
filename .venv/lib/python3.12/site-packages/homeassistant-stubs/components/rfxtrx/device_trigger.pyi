from . import DOMAIN as DOMAIN
from .const import EVENT_RFXTRX_EVENT as EVENT_RFXTRX_EVENT
from .helpers import async_get_device_object as async_get_device_object
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA, InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

CONF_SUBTYPE: str
CONF_TYPE_COMMAND: str
CONF_TYPE_STATUS: str
TRIGGER_SELECTION: Incomplete
TRIGGER_TYPES: Incomplete
TRIGGER_SCHEMA: Incomplete

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
