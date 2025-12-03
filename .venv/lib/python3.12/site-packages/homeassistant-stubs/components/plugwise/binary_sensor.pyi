from . import PlugwiseConfigEntry as PlugwiseConfigEntry
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from plugwise.constants import BinarySensorType as BinarySensorType
from typing import Any

SEVERITIES: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True)
class PlugwiseBinarySensorEntityDescription(BinarySensorEntityDescription):
    key: BinarySensorType

BINARY_SENSORS: tuple[PlugwiseBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseBinarySensorEntity(PlugwiseEntity, BinarySensorEntity):
    entity_description: PlugwiseBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, description: PlugwiseBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
