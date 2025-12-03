from . import AirQConfigEntry as AirQConfigEntry, AirQCoordinator as AirQCoordinator
from .const import ACTIVITY_BECQUEREL_PER_CUBIC_METER as ACTIVITY_BECQUEREL_PER_CUBIC_METER, CONCENTRATION_GRAMS_PER_CUBIC_METER as CONCENTRATION_GRAMS_PER_CUBIC_METER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER as CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class AirQEntityDescription(SensorEntityDescription):
    value: Callable[[dict], float | int | None]

SENSOR_TYPES: list[AirQEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: AirQConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirQSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: AirQEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, coordinator: AirQCoordinator, description: AirQEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
