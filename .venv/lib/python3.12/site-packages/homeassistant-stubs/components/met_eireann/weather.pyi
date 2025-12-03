from . import MetEireannWeatherData as MetEireannWeatherData
from .const import CONDITION_MAP as CONDITION_MAP, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, FORECAST_MAP as FORECAST_MAP
from _typeshed import Incomplete
from homeassistant.components.weather import ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, Forecast as Forecast, SingleCoordinatorWeatherEntity as SingleCoordinatorWeatherEntity, WeatherEntityFeature as WeatherEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from types import MappingProxyType
from typing import Any

_LOGGER: Incomplete

def format_condition(condition: str | None) -> str | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _calculate_unique_id(config: MappingProxyType[str, Any], hourly: bool) -> str: ...

class MetEireannWeather(SingleCoordinatorWeatherEntity[DataUpdateCoordinator[MetEireannWeatherData]]):
    _attr_attribution: str
    _attr_native_precipitation_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_native_temperature_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _config: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[MetEireannWeatherData], config: MappingProxyType[str, Any]) -> None: ...
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
    def wind_bearing(self) -> float | None: ...
    def _forecast(self, hourly: bool) -> list[Forecast]: ...
    @callback
    def _async_forecast_daily(self) -> list[Forecast]: ...
    @callback
    def _async_forecast_hourly(self) -> list[Forecast]: ...
