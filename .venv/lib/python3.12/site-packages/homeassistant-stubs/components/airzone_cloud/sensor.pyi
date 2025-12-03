import abc
from . import AirzoneCloudConfigEntry as AirzoneCloudConfigEntry
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneAidooEntity as AirzoneAidooEntity, AirzoneEntity as AirzoneEntity, AirzoneWebServerEntity as AirzoneWebServerEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfInformation as UnitOfInformation, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

AIDOO_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]
WEBSERVER_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]
ZONE_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneCloudConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneSensor(AirzoneEntity, SensorEntity, metaclass=abc.ABCMeta):
    @property
    def available(self) -> bool: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

class AirzoneAidooSensor(AirzoneAidooEntity, AirzoneSensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, aidoo_id: str, aidoo_data: dict[str, Any]) -> None: ...

class AirzoneWebServerSensor(AirzoneWebServerEntity, AirzoneSensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, ws_id: str, ws_data: dict[str, Any]) -> None: ...

class AirzoneZoneSensor(AirzoneZoneEntity, AirzoneSensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, zone_id: str, zone_data: dict[str, Any]) -> None: ...
