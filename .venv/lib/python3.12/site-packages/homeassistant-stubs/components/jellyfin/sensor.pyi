from . import JellyfinConfigEntry as JellyfinConfigEntry, JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from .entity import JellyfinServerEntity as JellyfinServerEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class JellyfinSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, dict[str, Any]]], StateType]

def _count_now_playing(data: dict[str, dict[str, Any]]) -> int: ...

SENSOR_TYPES: tuple[JellyfinSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: JellyfinConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JellyfinServerSensor(JellyfinServerEntity, SensorEntity):
    entity_description: JellyfinSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JellyfinDataUpdateCoordinator, description: JellyfinSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
