from . import PowerfoxConfigEntry as PowerfoxConfigEntry
from .coordinator import PowerfoxDataUpdateCoordinator as PowerfoxDataUpdateCoordinator
from .entity import PowerfoxEntity as PowerfoxEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from powerfox import Device as Device, PowerMeter, WaterMeter

@dataclass(frozen=True, kw_only=True)
class PowerfoxSensorEntityDescription[T: (PowerMeter, WaterMeter)](SensorEntityDescription):
    value_fn: Callable[[T], float | int | None]

SENSORS_POWER: tuple[PowerfoxSensorEntityDescription[PowerMeter], ...]
SENSORS_WATER: tuple[PowerfoxSensorEntityDescription[WaterMeter], ...]

async def async_setup_entry(hass: HomeAssistant, entry: PowerfoxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerfoxSensorEntity(PowerfoxEntity, SensorEntity):
    entity_description: PowerfoxSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PowerfoxDataUpdateCoordinator, device: Device, description: PowerfoxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
