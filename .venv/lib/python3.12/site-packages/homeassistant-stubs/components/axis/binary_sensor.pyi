from . import AxisConfigEntry as AxisConfigEntry
from .entity import AxisEventDescription as AxisEventDescription, AxisEventEntity as AxisEventEntity
from .hub import AxisHub as AxisHub
from _typeshed import Incomplete
from axis.interfaces.applications.fence_guard import FenceGuardHandler as FenceGuardHandler
from axis.interfaces.applications.loitering_guard import LoiteringGuardHandler as LoiteringGuardHandler
from axis.interfaces.applications.motion_guard import MotionGuardHandler as MotionGuardHandler
from axis.interfaces.applications.vmd4 import Vmd4Handler as Vmd4Handler
from axis.models.event import Event as Event
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later

@dataclass(frozen=True, kw_only=True)
class AxisBinarySensorDescription(AxisEventDescription, BinarySensorEntityDescription): ...

@callback
def event_id_is_int(event_id: str) -> bool: ...
@callback
def guard_suite_supported_fn(hub: AxisHub, event: Event) -> bool: ...
@callback
def object_analytics_supported_fn(hub: AxisHub, event: Event) -> bool: ...
@callback
def guard_suite_name_fn(handler: FenceGuardHandler | LoiteringGuardHandler | MotionGuardHandler | Vmd4Handler, event: Event, event_type: str) -> str: ...
@callback
def fence_guard_name_fn(hub: AxisHub, event: Event) -> str: ...
@callback
def loitering_guard_name_fn(hub: AxisHub, event: Event) -> str: ...
@callback
def motion_guard_name_fn(hub: AxisHub, event: Event) -> str: ...
@callback
def motion_detection_4_name_fn(hub: AxisHub, event: Event) -> str: ...
@callback
def object_analytics_name_fn(hub: AxisHub, event: Event) -> str: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AxisConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AxisBinarySensor(AxisEventEntity, BinarySensorEntity):
    entity_description: AxisBinarySensorDescription
    _attr_is_on: Incomplete
    cancel_scheduled_update: Callable[[], None] | None
    def __init__(self, hub: AxisHub, description: AxisBinarySensorDescription, event: Event) -> None: ...
    @callback
    def async_event_callback(self, event: Event) -> None: ...
