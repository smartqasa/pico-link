from .coordinator import TedeeConfigEntry as TedeeConfigEntry
from .entity import TedeeDescriptionEntity as TedeeDescriptionEntity
from aiotedee import TedeeLock as TedeeLock
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TedeeSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TedeeLock], float | None]

ENTITIES: tuple[TedeeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TedeeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TedeeSensorEntity(TedeeDescriptionEntity, SensorEntity):
    entity_description: TedeeSensorEntityDescription
    @property
    def native_value(self) -> float | None: ...
