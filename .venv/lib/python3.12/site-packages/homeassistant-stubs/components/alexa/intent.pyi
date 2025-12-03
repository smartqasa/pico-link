import enum
from .const import DOMAIN as DOMAIN, SYN_RESOLUTION_MATCH as SYN_RESOLUTION_MATCH
from _typeshed import Incomplete
from aiohttp.web import Response as Response
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components import http as http
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import intent as intent
from homeassistant.util.decorator import Registry as Registry
from typing import Any

_LOGGER: Incomplete
HANDLERS: Registry[str, Callable[[HomeAssistant, dict[str, Any]], Coroutine[Any, Any, dict[str, Any]]]]
INTENTS_API_ENDPOINT: str

class SpeechType(enum.StrEnum):
    plaintext = 'PlainText'
    ssml = 'SSML'

SPEECH_MAPPINGS: Incomplete

class CardType(enum.StrEnum):
    simple = 'Simple'
    link_account = 'LinkAccount'

@callback
def async_setup(hass: HomeAssistant) -> None: ...
async def async_setup_intents(hass: HomeAssistant) -> None: ...

class UnknownRequest(HomeAssistantError): ...

class AlexaIntentsView(http.HomeAssistantView):
    url = INTENTS_API_ENDPOINT
    name: str
    async def post(self, request: http.HomeAssistantRequest) -> Response | bytes: ...

def intent_error_response(hass: HomeAssistant, message: dict[str, Any], error: str) -> dict[str, Any]: ...
async def async_handle_message(hass: HomeAssistant, message: dict[str, Any]) -> dict[str, Any]: ...
async def async_handle_intent(hass: HomeAssistant, message: dict[str, Any]) -> dict[str, Any]: ...
def resolve_slot_data(key: str, request: dict[str, Any]) -> dict[str, str]: ...

class AlexaIntentResponse:
    hass: Incomplete
    speech: dict[str, Any] | None
    card: dict[str, Any] | None
    reprompt: dict[str, Any] | None
    session_attributes: dict[str, Any]
    should_end_session: bool
    variables: dict[str, Any]
    def __init__(self, hass: HomeAssistant, intent_info: dict[str, Any] | None) -> None: ...
    def add_card(self, card_type: CardType, title: str, content: str) -> None: ...
    def add_speech(self, speech_type: SpeechType, text: str) -> None: ...
    def add_reprompt(self, speech_type: SpeechType, text: str) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...
