import datetime
from . import RoborockConfigEntry as RoborockConfigEntry
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01
from .entity import RoborockCoordinatedEntityA01 as RoborockCoordinatedEntityA01, RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfArea as UnitOfArea, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from roborock.roborock_message import RoborockDataProtocol, RoborockDyadDataProtocol, RoborockZeoProtocol
from roborock.roborock_typing import DeviceProp as DeviceProp

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescription(SensorEntityDescription):
    value_fn: Callable[[DeviceProp], StateType | datetime.datetime]
    protocol_listener: RoborockDataProtocol | None = ...

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescriptionA01(SensorEntityDescription):
    data_protocol: RoborockDyadDataProtocol | RoborockZeoProtocol

def _dock_error_value_fn(properties: DeviceProp) -> str | None: ...

SENSOR_DESCRIPTIONS: Incomplete
A01_SENSOR_DESCRIPTIONS: list[RoborockSensorDescriptionA01]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockSensorEntity(RoborockCoordinatedEntityV1, SensorEntity):
    entity_description: RoborockSensorDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, description: RoborockSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime.datetime: ...

class RoborockSensorEntityA01(RoborockCoordinatedEntityA01, SensorEntity):
    entity_description: RoborockSensorDescriptionA01
    def __init__(self, coordinator: RoborockDataUpdateCoordinatorA01, description: RoborockSensorDescriptionA01) -> None: ...
    @property
    def native_value(self) -> StateType: ...
