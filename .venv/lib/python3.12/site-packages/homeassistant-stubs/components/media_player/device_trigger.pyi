import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA, entity as entity
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE, STATE_BUFFERING as STATE_BUFFERING, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

TRIGGER_TYPES: Incomplete
MEDIA_PLAYER_TRIGGER_SCHEMA: Incomplete
TRIGGER_SCHEMA: Incomplete

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
