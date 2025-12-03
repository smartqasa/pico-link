import dataclasses
from . import RadarrConfigEntry as RadarrConfigEntry
from .coordinator import RadarrDataUpdateCoordinator as RadarrDataUpdateCoordinator, T as T
from .entity import RadarrEntity as RadarrEntity
from _typeshed import Incomplete
from aiopyarr import Diskspace as Diskspace, RootFolder as RootFolder
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

def get_space(data: list[Diskspace], name: str) -> str: ...
def get_modified_description(description: RadarrSensorEntityDescription[T], mount: RootFolder) -> tuple[RadarrSensorEntityDescription[T], str]: ...

@dataclasses.dataclass(frozen=True)
class RadarrSensorEntityDescriptionMixIn(Generic[T]):
    value_fn: Callable[[T, str], str | int | datetime]

@dataclasses.dataclass(frozen=True)
class RadarrSensorEntityDescription(SensorEntityDescription, RadarrSensorEntityDescriptionMixIn[T], Generic[T]):
    description_fn: Callable[[RadarrSensorEntityDescription[T], RootFolder], tuple[RadarrSensorEntityDescription[T], str] | None] | None = ...

SENSOR_TYPES: dict[str, RadarrSensorEntityDescription[Any]]
BYTE_SIZES: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: RadarrConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RadarrSensor(RadarrEntity[T], SensorEntity):
    coordinator: RadarrDataUpdateCoordinator[T]
    entity_description: RadarrSensorEntityDescription[T]
    folder_name: Incomplete
    def __init__(self, coordinator: RadarrDataUpdateCoordinator[T], description: RadarrSensorEntityDescription[T], folder_name: str = '') -> None: ...
    @property
    def native_value(self) -> str | int | datetime: ...
