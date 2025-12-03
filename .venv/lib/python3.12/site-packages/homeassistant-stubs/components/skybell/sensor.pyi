from .entity import DOMAIN as DOMAIN, SkybellEntity as SkybellEntity
from aioskybell import SkybellDevice as SkybellDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class SkybellSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SkybellDevice], StateType | datetime]

SENSOR_TYPES: tuple[SkybellSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SkybellSensor(SkybellEntity, SensorEntity):
    entity_description: SkybellSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...
