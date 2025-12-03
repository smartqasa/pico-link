from . import SchlageConfigEntry as SchlageConfigEntry
from .coordinator import LockData as LockData, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from .entity import SchlageEntity as SchlageEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class SchlageBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[LockData], bool]

_DESCRIPTIONS: tuple[SchlageBinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: SchlageConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SchlageBinarySensor(SchlageEntity, BinarySensorEntity):
    entity_description: SchlageBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SchlageDataUpdateCoordinator, description: SchlageBinarySensorEntityDescription, device_id: str) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
