from .const import DOMAIN as DOMAIN
from .device import DoorbirdEvent as DoorbirdEvent
from .entity import DoorBirdEntity as DoorBirdEntity
from .models import DoorBirdConfigEntry as DoorBirdConfigEntry, DoorBirdData as DoorBirdData
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

EVENT_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: DoorBirdConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DoorBirdEventEntity(DoorBirdEntity, EventEntity):
    entity_description: EventEntityDescription
    _attr_has_entity_name: bool
    _doorbird_event: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, door_bird_data: DoorBirdData, doorbird_event: DoorbirdEvent, entity_description: EventEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self) -> None: ...
