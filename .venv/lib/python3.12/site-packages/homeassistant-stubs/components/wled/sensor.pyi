from . import WLEDConfigEntry as WLEDConfigEntry
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from wled import Device as WLEDDevice

@dataclass(frozen=True, kw_only=True)
class WLEDSensorEntityDescription(SensorEntityDescription):
    exists_fn: Callable[[WLEDDevice], bool] = ...
    value_fn: Callable[[WLEDDevice], datetime | StateType]

SENSORS: tuple[WLEDSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDSensorEntity(WLEDEntity, SensorEntity):
    entity_description: WLEDSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, description: WLEDSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime | StateType: ...
