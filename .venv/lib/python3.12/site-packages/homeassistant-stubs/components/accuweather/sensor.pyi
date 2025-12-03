from .const import API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_CATEGORY as ATTR_CATEGORY, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_ENGLISH as ATTR_ENGLISH, ATTR_LEVEL as ATTR_LEVEL, ATTR_SPEED as ATTR_SPEED, ATTR_VALUE as ATTR_VALUE, MAX_FORECAST_DAYS as MAX_FORECAST_DAYS
from .coordinator import AccuWeatherConfigEntry as AccuWeatherConfigEntry, AccuWeatherDailyForecastDataUpdateCoordinator as AccuWeatherDailyForecastDataUpdateCoordinator, AccuWeatherObservationDataUpdateCoordinator as AccuWeatherObservationDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_CUBIC_METER as CONCENTRATION_PARTS_PER_CUBIC_METER, PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AccuWeatherSensorDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], str | int | float | None]
    attr_fn: Callable[[dict[str, Any]], dict[str, Any]] = ...

FORECAST_SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]
SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherSensor(CoordinatorEntity[AccuWeatherObservationDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: AccuWeatherSensorDescription
    _sensor_data: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AccuWeatherObservationDataUpdateCoordinator, description: AccuWeatherSensorDescription) -> None: ...
    @property
    def native_value(self) -> str | int | float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @staticmethod
    def _get_sensor_data(sensors: dict[str, Any], kind: str) -> Any: ...

class AccuWeatherForecastSensor(CoordinatorEntity[AccuWeatherDailyForecastDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: AccuWeatherSensorDescription
    _sensor_data: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_placeholders: Incomplete
    forecast_day: Incomplete
    def __init__(self, coordinator: AccuWeatherDailyForecastDataUpdateCoordinator, description: AccuWeatherSensorDescription, forecast_day: int) -> None: ...
    @property
    def native_value(self) -> str | int | float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @staticmethod
    def _get_sensor_data(sensors: list[dict[str, Any]], kind: str, forecast_day: int) -> Any: ...
