from . import BAFConfigEntry as BAFConfigEntry
from .entity import BAFDescriptionEntity as BAFDescriptionEntity
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class BAFSensorDescription(SensorEntityDescription):
    value_fn: Callable[[Device], int | float | str | None]

AUTO_COMFORT_SENSORS: Incomplete
DEFINED_ONLY_SENSORS: Incomplete
FAN_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BAFConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFSensor(BAFDescriptionEntity, SensorEntity):
    entity_description: BAFSensorDescription
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
