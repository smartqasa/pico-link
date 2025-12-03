from ..entity import AxisEventDescription as AxisEventDescription, AxisEventEntity as AxisEventEntity
from .hub import AxisHub as AxisHub
from _typeshed import Incomplete
from axis.models.event import Event as Event, EventTopic
from homeassistant.core import callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class AxisEntityLoader:
    hub: Incomplete
    registered_events: set[tuple[str, EventTopic, str]]
    topic_to_entity: dict[EventTopic, list[tuple[AddEntitiesCallback, type[AxisEventEntity], AxisEventDescription]]]
    def __init__(self, hub: AxisHub) -> None: ...
    @callback
    def register_platform(self, async_add_entities: AddEntitiesCallback, entity_class: type[AxisEventEntity], descriptions: tuple[AxisEventDescription, ...]) -> None: ...
    @callback
    def _create_entities_from_event(self, event: Event) -> None: ...
    @callback
    def initialize_platforms(self) -> None: ...
