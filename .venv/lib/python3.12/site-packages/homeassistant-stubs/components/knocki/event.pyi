from . import KnockiConfigEntry as KnockiConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from knocki import Event as Event, KnockiClient as KnockiClient, Trigger as Trigger

async def async_setup_entry(hass: HomeAssistant, entry: KnockiConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

EVENT_TRIGGERED: str

class KnockiTrigger(EventEntity):
    _attr_event_types: Incomplete
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_translation_key: str
    _trigger: Incomplete
    _client: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, trigger: Trigger, client: KnockiClient) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_event(self, event: Event) -> None: ...
