from .const import DOMAIN as DOMAIN, WMO_TO_HA_CONDITION_MAP as WMO_TO_HA_CONDITION_MAP
from _typeshed import Incomplete
from homeassistant.components.weather import ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_NATIVE_PRECIPITATION as ATTR_FORECAST_NATIVE_PRECIPITATION, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_TEMP_LOW as ATTR_FORECAST_NATIVE_TEMP_LOW, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, Forecast as Forecast, SingleCoordinatorWeatherEntity as SingleCoordinatorWeatherEntity, WeatherEntityFeature as WeatherEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from open_meteo import Forecast as OpenMeteoForecast

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenMeteoWeatherEntity(SingleCoordinatorWeatherEntity[DataUpdateCoordinator[OpenMeteoForecast]]):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_native_precipitation_unit: Incomplete
    _attr_native_temperature_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry: ConfigEntry, coordinator: DataUpdateCoordinator[OpenMeteoForecast]) -> None: ...
    @property
    def condition(self) -> str | None: ...
    @property
    def native_temperature(self) -> float | None: ...
    @property
    def native_wind_speed(self) -> float | None: ...
    @property
    def wind_bearing(self) -> float | str | None: ...
    @callback
    def _async_forecast_daily(self) -> list[Forecast] | None: ...
    @callback
    def _async_forecast_hourly(self) -> list[Forecast] | None: ...
