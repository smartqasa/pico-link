from . import NanoleafConfigEntry as NanoleafConfigEntry, NanoleafCoordinator as NanoleafCoordinator
from .const import TOUCH_MODELS as TOUCH_MODELS
from .entity import NanoleafEntity as NanoleafEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: NanoleafConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafGestureEvent(NanoleafEntity, EventEntity):
    _attr_event_types: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: NanoleafCoordinator) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, gesture: str) -> None: ...
