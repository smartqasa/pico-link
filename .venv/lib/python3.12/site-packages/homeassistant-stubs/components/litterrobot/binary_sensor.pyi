from . import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import Robot
from typing import Generic

@dataclass(frozen=True)
class RequiredKeysMixin(Generic[_RobotT]):
    is_on_fn: Callable[[_RobotT], bool]

@dataclass(frozen=True)
class RobotBinarySensorEntityDescription(BinarySensorEntityDescription, RequiredKeysMixin[_RobotT]): ...

class LitterRobotBinarySensorEntity(LitterRobotEntity[_RobotT], BinarySensorEntity):
    entity_description: RobotBinarySensorEntityDescription[_RobotT]
    @property
    def is_on(self) -> bool: ...

BINARY_SENSOR_MAP: dict[type[Robot], tuple[RobotBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
