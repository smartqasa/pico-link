from . import AirVisualProConfigEntry as AirVisualProConfigEntry
from .entity import AirVisualProEntity as AirVisualProEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class AirVisualProMeasurementDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]], float | int]

SENSOR_DESCRIPTIONS: Incomplete

@callback
def async_get_aqi_locale(settings: dict[str, Any]) -> str: ...
async def async_setup_entry(hass: HomeAssistant, entry: AirVisualProConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirVisualProSensor(AirVisualProEntity, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: AirVisualProMeasurementDescription
    @property
    def native_value(self) -> float | int: ...
