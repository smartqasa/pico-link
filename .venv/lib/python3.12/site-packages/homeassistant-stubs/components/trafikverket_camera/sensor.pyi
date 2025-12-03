from . import TVCameraConfigEntry as TVCameraConfigEntry
from .coordinator import CameraData as CameraData
from .entity import TrafikverketCameraNonCameraEntity as TrafikverketCameraNonCameraEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import DEGREE as DEGREE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TVCameraSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[CameraData], StateType | datetime]

SENSOR_TYPES: tuple[TVCameraSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TVCameraConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TrafikverketCameraSensor(TrafikverketCameraNonCameraEntity, SensorEntity):
    entity_description: TVCameraSensorEntityDescription
    _attr_native_value: Incomplete
    @callback
    def _update_attr(self) -> None: ...
