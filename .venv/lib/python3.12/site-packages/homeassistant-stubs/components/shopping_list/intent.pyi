from . import DOMAIN as DOMAIN, EVENT_SHOPPING_LIST_UPDATED as EVENT_SHOPPING_LIST_UPDATED
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_ADD_ITEM: str
INTENT_LAST_ITEMS: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class AddItemIntent(intent.IntentHandler):
    intent_type = INTENT_ADD_ITEM
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class ListTopItemsIntent(intent.IntentHandler):
    intent_type = INTENT_LAST_ITEMS
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
