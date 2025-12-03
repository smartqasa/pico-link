from .const import BUTTON as BUTTON, BUTTON_PRESS as BUTTON_PRESS, BUTTON_PRESS_DOUBLE_LONG as BUTTON_PRESS_DOUBLE_LONG, BUTTON_PRESS_LONG as BUTTON_PRESS_LONG, CONF_SUBTYPE as CONF_SUBTYPE, CUBE as CUBE, DIMMER as DIMMER, DOMAIN as DOMAIN, DOUBLE_BUTTON as DOUBLE_BUTTON, DOUBLE_BUTTON_PRESS_DOUBLE_LONG as DOUBLE_BUTTON_PRESS_DOUBLE_LONG, ERROR as ERROR, EVENT_CLASS as EVENT_CLASS, EVENT_CLASS_BUTTON as EVENT_CLASS_BUTTON, EVENT_CLASS_CUBE as EVENT_CLASS_CUBE, EVENT_CLASS_DIMMER as EVENT_CLASS_DIMMER, EVENT_CLASS_ERROR as EVENT_CLASS_ERROR, EVENT_CLASS_FINGERPRINT as EVENT_CLASS_FINGERPRINT, EVENT_CLASS_LOCK as EVENT_CLASS_LOCK, EVENT_CLASS_MOTION as EVENT_CLASS_MOTION, EVENT_TYPE as EVENT_TYPE, FINGERPRINT as FINGERPRINT, LOCK as LOCK, LOCK_FINGERPRINT as LOCK_FINGERPRINT, MOTION as MOTION, MOTION_DEVICE as MOTION_DEVICE, REMOTE as REMOTE, REMOTE_BATHROOM as REMOTE_BATHROOM, REMOTE_FAN as REMOTE_FAN, REMOTE_VENFAN as REMOTE_VENFAN, TRIPPLE_BUTTON as TRIPPLE_BUTTON, TRIPPLE_BUTTON_PRESS_DOUBLE_LONG as TRIPPLE_BUTTON_PRESS_DOUBLE_LONG, XIAOMI_BLE_EVENT as XIAOMI_BLE_EVENT
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

TRIGGERS_BY_TYPE: Incomplete
EVENT_TYPES: Incomplete

@dataclass
class TriggerModelData:
    event_class: str
    event_types: list[str]
    triggers: list[str]

TRIGGER_MODEL_DATA: Incomplete
MODEL_DATA: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
def _async_trigger_model_data(hass: HomeAssistant, device_id: str) -> TriggerModelData | None: ...
