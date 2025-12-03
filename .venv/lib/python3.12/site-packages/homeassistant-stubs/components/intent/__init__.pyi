from .const import DOMAIN as DOMAIN
from .timers import TimerEventType as TimerEventType, TimerInfo as TimerInfo, async_device_supports_timers as async_device_supports_timers, async_register_timer_handler as async_register_timer_handler
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components import http
from homeassistant.core import HomeAssistant, State
from homeassistant.helpers import intent
from typing import Any, Protocol

__all__ = ['async_register_timer_handler', 'async_device_supports_timers', 'TimerInfo', 'TimerEventType', 'DOMAIN']

class IntentPlatformProtocol(Protocol):
    async def async_setup_intents(self, hass: HomeAssistant) -> None: ...

class OnOffIntentHandler(intent.ServiceIntentHandler):
    async def async_call_service(self, domain: str, service: str, intent_obj: intent.Intent, state: State) -> None: ...

class GetStateIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class NevermindIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class SetPositionIntentHandler(intent.DynamicServiceIntentHandler):
    def __init__(self) -> None: ...
    def get_domain_and_service(self, intent_obj: intent.Intent, state: State) -> tuple[str, str]: ...

class GetCurrentDateIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class GetCurrentTimeIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class RespondIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class IntentHandleView(http.HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
