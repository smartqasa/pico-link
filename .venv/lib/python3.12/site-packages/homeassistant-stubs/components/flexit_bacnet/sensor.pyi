from . import FlexitCoordinator as FlexitCoordinator
from .const import DOMAIN as DOMAIN
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from flexit_bacnet import FlexitBACnet as FlexitBACnet
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(kw_only=True, frozen=True)
class FlexitSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[FlexitBACnet], float]

SENSOR_TYPES: tuple[FlexitSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FlexitSensor(FlexitEntity, SensorEntity):
    entity_description: FlexitSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitCoordinator, entity_description: FlexitSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
