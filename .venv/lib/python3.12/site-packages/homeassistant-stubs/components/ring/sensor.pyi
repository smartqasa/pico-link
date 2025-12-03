from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import DeprecatedInfo as DeprecatedInfo, RingDeviceT as RingDeviceT, RingEntity as RingEntity, RingEntityDescription as RingEntityDescription, async_check_create_deprecated as async_check_create_deprecated
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, Platform as Platform, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from ring_doorbell import RingEventKind, RingGeneric
from typing import Any, Generic

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingSensor(RingEntity[RingDeviceT], SensorEntity):
    entity_description: RingSensorEntityDescription[RingDeviceT]
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: RingDataCoordinator, description: RingSensorEntityDescription[RingDeviceT]) -> None: ...
    _device: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...

def _get_last_event(history_data: list[dict[str, Any]], kind: RingEventKind | None) -> dict[str, Any] | None: ...
def _get_last_event_attrs(history_data: list[dict[str, Any]], kind: RingEventKind | None) -> dict[str, Any] | None: ...

@dataclass(frozen=True, kw_only=True)
class RingSensorEntityDescription(SensorEntityDescription, RingEntityDescription, Generic[RingDeviceT]):
    value_fn: Callable[[RingDeviceT], StateType] = ...
    exists_fn: Callable[[RingGeneric], bool] = ...
    extra_state_attributes_fn: Callable[[RingDeviceT], dict[str, Any] | None] = ...

SENSOR_TYPES: tuple[RingSensorEntityDescription[Any], ...]
