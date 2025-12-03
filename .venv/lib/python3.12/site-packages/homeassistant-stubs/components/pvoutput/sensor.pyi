from .const import CONF_SYSTEM_ID as CONF_SYSTEM_ID, DOMAIN as DOMAIN
from .coordinator import PVOutputDataUpdateCoordinator as PVOutputDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pvo import Status as Status, System as System

@dataclass(frozen=True, kw_only=True)
class PVOutputSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Status], int | float | None]

SENSORS: tuple[PVOutputSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PVOutputSensorEntity(CoordinatorEntity[PVOutputDataUpdateCoordinator], SensorEntity):
    entity_description: PVOutputSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: PVOutputDataUpdateCoordinator, description: PVOutputSensorEntityDescription, system_id: str, system: System) -> None: ...
    @property
    def native_value(self) -> int | float | None: ...
