from . import get_device_info as get_device_info
from .const import ATTRIBUTION as ATTRIBUTION, CONDITION_MAP as CONDITION_MAP, DOMAIN as DOMAIN, METOFFICE_COORDINATES as METOFFICE_COORDINATES, METOFFICE_DAILY_COORDINATOR as METOFFICE_DAILY_COORDINATOR, METOFFICE_HOURLY_COORDINATOR as METOFFICE_HOURLY_COORDINATOR, METOFFICE_NAME as METOFFICE_NAME, MODE_DAILY as MODE_DAILY
from .data import MetOfficeData as MetOfficeData
from _typeshed import Incomplete
from datapoint.Timestep import Timestep as Timestep
from homeassistant.components.weather import ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_PRECIPITATION_PROBABILITY as ATTR_FORECAST_PRECIPITATION_PROBABILITY, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, CoordinatorWeatherEntity as CoordinatorWeatherEntity, Forecast as Forecast, WeatherEntityFeature as WeatherEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _build_forecast_data(timestep: Timestep) -> Forecast: ...
def _calculate_unique_id(coordinates: str, use_3hourly: bool) -> str: ...

class MetOfficeWeather(CoordinatorWeatherEntity[TimestampDataUpdateCoordinator[MetOfficeData], TimestampDataUpdateCoordinator[MetOfficeData]]):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_native_temperature_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_device_info: Incomplete
    _attr_name: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator_daily: TimestampDataUpdateCoordinator[MetOfficeData], coordinator_hourly: TimestampDataUpdateCoordinator[MetOfficeData], hass_data: dict[str, Any]) -> None: ...
    @property
    def condition(self) -> str | None: ...
    @property
    def native_temperature(self) -> float | None: ...
    @property
    def native_pressure(self) -> float | None: ...
    @property
    def humidity(self) -> float | None: ...
    @property
    def native_wind_speed(self) -> float | None: ...
    @property
    def wind_bearing(self) -> str | None: ...
    @callback
    def _async_forecast_daily(self) -> list[Forecast] | None: ...
    @callback
    def _async_forecast_hourly(self) -> list[Forecast] | None: ...
