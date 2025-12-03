from . import TechnoVEConfigEntry as TechnoVEConfigEntry
from .coordinator import TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from .entity import TechnoVEEntity as TechnoVEEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from technove import Station as TechnoVEStation

STATUS_TYPE: Incomplete

@dataclass(frozen=True, kw_only=True)
class TechnoVESensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TechnoVEStation], StateType]

SENSORS: tuple[TechnoVESensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TechnoVEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TechnoVESensorEntity(TechnoVEEntity, SensorEntity):
    entity_description: TechnoVESensorEntityDescription
    def __init__(self, coordinator: TechnoVEDataUpdateCoordinator, description: TechnoVESensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
