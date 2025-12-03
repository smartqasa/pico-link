from . import DOMAIN as DOMAIN, INTENT_GET_WEATHER as INTENT_GET_WEATHER
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers import intent as intent

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class GetWeatherIntent(intent.IntentHandler):
    intent_type = INTENT_GET_WEATHER
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
