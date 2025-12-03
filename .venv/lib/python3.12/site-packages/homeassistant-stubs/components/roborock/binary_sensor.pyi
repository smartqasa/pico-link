from . import RoborockConfigEntry as RoborockConfigEntry
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from roborock.roborock_typing import DeviceProp as DeviceProp

@dataclass(frozen=True, kw_only=True)
class RoborockBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[DeviceProp], bool | int | None]

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockBinarySensorEntity(RoborockCoordinatedEntityV1, BinarySensorEntity):
    entity_description: RoborockBinarySensorDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, description: RoborockBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
