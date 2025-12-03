from . import DEFAULT_METHODS as DEFAULT_METHODS, DOMAIN as DOMAIN, SUPPORTED_METHODS as SUPPORTED_METHODS, async_register as async_register, async_unregister as async_unregister
from _typeshed import Incomplete
from aiohttp import web as web
from dataclasses import dataclass
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
DEPENDENCIES: Incomplete
CONF_ALLOWED_METHODS: str
CONF_LOCAL_ONLY: str
TRIGGER_SCHEMA: Incomplete
WEBHOOK_TRIGGERS: Incomplete

@dataclass(slots=True)
class TriggerInstance:
    trigger_info: TriggerInfo
    job: HassJob

async def _handle_webhook(hass: HomeAssistant, webhook_id: str, request: web.Request) -> None: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
