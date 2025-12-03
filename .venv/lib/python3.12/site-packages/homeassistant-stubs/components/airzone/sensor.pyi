from . import AirzoneConfigEntry as AirzoneConfigEntry
from .const import TEMP_UNIT_LIB_TO_HASS as TEMP_UNIT_LIB_TO_HASS
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneEntity as AirzoneEntity, AirzoneHotWaterEntity as AirzoneHotWaterEntity, AirzoneWebServerEntity as AirzoneWebServerEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

HOT_WATER_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]
WEBSERVER_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]
ZONE_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneSensor(AirzoneEntity, SensorEntity):
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

class AirzoneHotWaterSensor(AirzoneHotWaterEntity, AirzoneSensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, entry: ConfigEntry) -> None: ...

class AirzoneWebServerSensor(AirzoneWebServerEntity, AirzoneSensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, entry: ConfigEntry) -> None: ...

class AirzoneZoneSensor(AirzoneZoneEntity, AirzoneSensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, entry: ConfigEntry, system_zone_id: str, zone_data: dict[str, Any]) -> None: ...
