from .const import DOMAIN as DOMAIN
from .schema import ga_validator as ga_validator
from .telegrams import SIGNAL_KNX_TELEGRAM as SIGNAL_KNX_TELEGRAM, TelegramDict as TelegramDict, decode_telegram_payload as decode_telegram_payload
from .validation import dpt_base_type_validator as dpt_base_type_validator
from _typeshed import Incomplete
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from typing import Final
from xknx.telegram import Telegram as Telegram
from xknx.telegram.address import DeviceGroupAddress as DeviceGroupAddress

TRIGGER_TELEGRAM: Final[str]
PLATFORM_TYPE_TRIGGER_TELEGRAM: Final[Incomplete]
CONF_KNX_DESTINATION: Final[str]
CONF_KNX_GROUP_VALUE_WRITE: Final[str]
CONF_KNX_GROUP_VALUE_READ: Final[str]
CONF_KNX_GROUP_VALUE_RESPONSE: Final[str]
CONF_KNX_INCOMING: Final[str]
CONF_KNX_OUTGOING: Final[str]
TELEGRAM_TRIGGER_SCHEMA: VolDictType
TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
