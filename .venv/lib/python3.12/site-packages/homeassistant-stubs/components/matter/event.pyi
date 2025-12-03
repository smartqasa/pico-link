from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from matter_server.common.models import EventType, MatterNodeEvent as MatterNodeEvent
from typing import Any

SwitchFeature: Incomplete
EVENT_TYPES_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterEventEntity(MatterEntity, EventEntity):
    _attr_event_types: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_from_device(self) -> None: ...
    @callback
    def _on_matter_node_event(self, event: EventType, data: MatterNodeEvent) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
