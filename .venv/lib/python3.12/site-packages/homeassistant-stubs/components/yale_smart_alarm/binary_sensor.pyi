from . import YaleConfigEntry as YaleConfigEntry
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleAlarmEntity as YaleAlarmEntity, YaleEntity as YaleEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: YaleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleDoorSensor(YaleEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class YaleDoorBatterySensor(YaleEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, data: dict) -> None: ...
    @property
    def is_on(self) -> bool: ...

class YaleProblemSensor(YaleAlarmEntity, BinarySensorEntity):
    entity_description: BinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, entity_description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
