from .device_info import NestDeviceInfo as NestDeviceInfo
from .events import EVENT_CAMERA_MOTION as EVENT_CAMERA_MOTION, EVENT_CAMERA_PERSON as EVENT_CAMERA_PERSON, EVENT_CAMERA_SOUND as EVENT_CAMERA_SOUND, EVENT_DOORBELL_CHIME as EVENT_DOORBELL_CHIME, EVENT_NAME_MAP as EVENT_NAME_MAP
from .types import NestConfigEntry as NestConfigEntry
from _typeshed import Incomplete
from dataclasses import dataclass
from google_nest_sdm.device import Device as Device
from google_nest_sdm.event import EventMessage as EventMessage, EventType
from google_nest_sdm.traits import TraitType
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

@dataclass(kw_only=True, frozen=True)
class NestEventEntityDescription(EventEntityDescription):
    trait_types: list[TraitType]
    api_event_types: list[EventType]
    event_types: list[str]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NestConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NestTraitEventEntity(EventEntity):
    entity_description: NestEventEntityDescription
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entity_description: NestEventEntityDescription, device: Device) -> None: ...
    async def _async_handle_event(self, event_message: EventMessage) -> None: ...
    async def async_added_to_hass(self) -> None: ...
