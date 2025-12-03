import voluptuous as vol
from . import BinarySensorDeviceClass as BinarySensorDeviceClass, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_automation import CONF_IS_OFF as CONF_IS_OFF, CONF_IS_ON as CONF_IS_ON
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_STATE as CONF_STATE, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.entity import get_device_class as get_device_class
from homeassistant.helpers.typing import ConfigType as ConfigType

DEVICE_CLASS_NONE: str
CONF_IS_BAT_LOW: str
CONF_IS_NOT_BAT_LOW: str
CONF_IS_CHARGING: str
CONF_IS_NOT_CHARGING: str
CONF_IS_CO: str
CONF_IS_NO_CO: str
CONF_IS_COLD: str
CONF_IS_NOT_COLD: str
CONF_IS_CONNECTED: str
CONF_IS_NOT_CONNECTED: str
CONF_IS_GAS: str
CONF_IS_NO_GAS: str
CONF_IS_HOT: str
CONF_IS_NOT_HOT: str
CONF_IS_LIGHT: str
CONF_IS_NO_LIGHT: str
CONF_IS_LOCKED: str
CONF_IS_NOT_LOCKED: str
CONF_IS_MOIST: str
CONF_IS_NOT_MOIST: str
CONF_IS_MOTION: str
CONF_IS_NO_MOTION: str
CONF_IS_MOVING: str
CONF_IS_NOT_MOVING: str
CONF_IS_OCCUPIED: str
CONF_IS_NOT_OCCUPIED: str
CONF_IS_PLUGGED_IN: str
CONF_IS_NOT_PLUGGED_IN: str
CONF_IS_POWERED: str
CONF_IS_NOT_POWERED: str
CONF_IS_PRESENT: str
CONF_IS_NOT_PRESENT: str
CONF_IS_PROBLEM: str
CONF_IS_NO_PROBLEM: str
CONF_IS_RUNNING: str
CONF_IS_NOT_RUNNING: str
CONF_IS_UNSAFE: str
CONF_IS_NOT_UNSAFE: str
CONF_IS_SMOKE: str
CONF_IS_NO_SMOKE: str
CONF_IS_SOUND: str
CONF_IS_NO_SOUND: str
CONF_IS_TAMPERED: str
CONF_IS_NOT_TAMPERED: str
CONF_IS_UPDATE: str
CONF_IS_NO_UPDATE: str
CONF_IS_VIBRATION: str
CONF_IS_NO_VIBRATION: str
CONF_IS_OPEN: str
CONF_IS_NOT_OPEN: str
IS_ON: Incomplete
IS_OFF: Incomplete
ENTITY_CONDITIONS: Incomplete
CONDITION_SCHEMA: Incomplete

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
@callback
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
