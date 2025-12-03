from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

def round_storage(value: int) -> float: ...
def truncate_url(value: StateType) -> tuple[StateType, dict[str, Any]]: ...

@dataclass(frozen=True)
class FullySensorEntityDescription(SensorEntityDescription):
    round_state_value: bool = ...
    state_fn: Callable[[StateType], tuple[StateType, dict[str, Any]]] | None = ...

SENSORS: tuple[FullySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullySensor(FullyKioskEntity, SensorEntity):
    entity_description: FullySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, sensor: FullySensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
