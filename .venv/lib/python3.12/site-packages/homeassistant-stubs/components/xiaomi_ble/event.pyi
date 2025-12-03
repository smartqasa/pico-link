from . import format_discovered_event_class as format_discovered_event_class, format_event_dispatcher_name as format_event_dispatcher_name
from .const import DOMAIN as DOMAIN, EVENT_CLASS_BUTTON as EVENT_CLASS_BUTTON, EVENT_CLASS_CUBE as EVENT_CLASS_CUBE, EVENT_CLASS_DIMMER as EVENT_CLASS_DIMMER, EVENT_CLASS_ERROR as EVENT_CLASS_ERROR, EVENT_CLASS_FINGERPRINT as EVENT_CLASS_FINGERPRINT, EVENT_CLASS_LOCK as EVENT_CLASS_LOCK, EVENT_CLASS_MOTION as EVENT_CLASS_MOTION, EVENT_PROPERTIES as EVENT_PROPERTIES, EVENT_TYPE as EVENT_TYPE, XiaomiBleEvent as XiaomiBleEvent
from .types import XiaomiBLEConfigEntry as XiaomiBLEConfigEntry
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

DESCRIPTIONS_BY_EVENT_CLASS: Incomplete

class XiaomiEventEntity(EventEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _update_signal: Incomplete
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, address: str, event_class: str, event: XiaomiBleEvent | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: XiaomiBleEvent) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: XiaomiBLEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
