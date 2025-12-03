from . import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_LIST_ADD_ITEM: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class ListAddItemIntent(intent.IntentHandler):
    intent_type = INTENT_LIST_ADD_ITEM
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
