from . import SensiboConfigEntry as SensiboConfigEntry
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, SensiboMotionBaseEntity as SensiboMotionBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import MotionSensor as MotionSensor, SensiboDevice as SensiboDevice

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SensiboMotionBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[MotionSensor], bool | None]

@dataclass(frozen=True, kw_only=True)
class SensiboDeviceBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[SensiboDevice], bool | None]

FILTER_CLEAN_REQUIRED_DESCRIPTION: Incomplete
MOTION_SENSOR_TYPES: tuple[SensiboMotionBinarySensorEntityDescription, ...]
MOTION_DEVICE_SENSOR_TYPES: tuple[SensiboDeviceBinarySensorEntityDescription, ...]
DEVICE_SENSOR_TYPES: tuple[SensiboDeviceBinarySensorEntityDescription, ...]
PURE_SENSOR_TYPES: tuple[SensiboDeviceBinarySensorEntityDescription, ...]
DESCRIPTION_BY_MODELS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboMotionSensor(SensiboMotionBaseEntity, BinarySensorEntity):
    entity_description: SensiboMotionBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, sensor_id: str, sensor_data: MotionSensor, entity_description: SensiboMotionBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class SensiboDeviceSensor(SensiboDeviceBaseEntity, BinarySensorEntity):
    entity_description: SensiboDeviceBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
