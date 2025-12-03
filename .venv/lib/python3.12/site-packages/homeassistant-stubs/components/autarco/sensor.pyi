from . import AutarcoConfigEntry as AutarcoConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AutarcoDataUpdateCoordinator as AutarcoDataUpdateCoordinator
from _typeshed import Incomplete
from autarco import Battery as Battery, Inverter as Inverter, Solar as Solar
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class AutarcoBatterySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Battery], StateType]

SENSORS_BATTERY: tuple[AutarcoBatterySensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class AutarcoSolarSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Solar], StateType]

SENSORS_SOLAR: tuple[AutarcoSolarSensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class AutarcoInverterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Inverter], StateType]

SENSORS_INVERTER: tuple[AutarcoInverterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AutarcoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutarcoBatterySensorEntity(CoordinatorEntity[AutarcoDataUpdateCoordinator], SensorEntity):
    entity_description: AutarcoBatterySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: AutarcoDataUpdateCoordinator, description: AutarcoBatterySensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class AutarcoSolarSensorEntity(CoordinatorEntity[AutarcoDataUpdateCoordinator], SensorEntity):
    entity_description: AutarcoSolarSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: AutarcoDataUpdateCoordinator, description: AutarcoSolarSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class AutarcoInverterSensorEntity(CoordinatorEntity[AutarcoDataUpdateCoordinator], SensorEntity):
    entity_description: AutarcoInverterSensorEntityDescription
    _attr_has_entity_name: bool
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: AutarcoDataUpdateCoordinator, description: AutarcoInverterSensorEntityDescription, serial_number: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...
