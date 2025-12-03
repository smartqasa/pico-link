from . import ATTR_AVAILABLE_MODES as ATTR_AVAILABLE_MODES, ATTR_HUMIDITY as ATTR_HUMIDITY, DOMAIN as DOMAIN, HumidifierEntityFeature as HumidifierEntityFeature, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_MODE as SERVICE_SET_MODE, SERVICE_TURN_ON as SERVICE_TURN_ON
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE, STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_HUMIDITY: str
INTENT_MODE: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class HumidityHandler(intent.IntentHandler):
    intent_type = INTENT_HUMIDITY
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class SetModeHandler(intent.IntentHandler):
    intent_type = INTENT_MODE
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
