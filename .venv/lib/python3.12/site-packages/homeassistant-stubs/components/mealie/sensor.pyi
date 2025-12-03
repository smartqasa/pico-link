from .coordinator import MealieConfigEntry as MealieConfigEntry, MealieStatisticsCoordinator as MealieStatisticsCoordinator
from .entity import MealieEntity as MealieEntity
from _typeshed import Incomplete
from aiomealie import Statistics as Statistics
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class MealieStatisticsSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Statistics], StateType]

SENSOR_TYPES: tuple[MealieStatisticsSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: MealieConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MealieStatisticSensors(MealieEntity, SensorEntity):
    entity_description: MealieStatisticsSensorEntityDescription
    coordinator: MealieStatisticsCoordinator
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: MealieStatisticsCoordinator, description: MealieStatisticsSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
