from .const import API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_SPEED as ATTR_SPEED, ATTR_VALUE as ATTR_VALUE, CONDITION_MAP as CONDITION_MAP
from .coordinator import AccuWeatherConfigEntry as AccuWeatherConfigEntry, AccuWeatherDailyForecastDataUpdateCoordinator as AccuWeatherDailyForecastDataUpdateCoordinator, AccuWeatherData as AccuWeatherData, AccuWeatherObservationDataUpdateCoordinator as AccuWeatherObservationDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.weather import ATTR_FORECAST_CLOUD_COVERAGE as ATTR_FORECAST_CLOUD_COVERAGE, ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_HUMIDITY as ATTR_FORECAST_HUMIDITY, ATTR_FORECAST_NATIVE_APPARENT_TEMP as ATTR_FORECAST_NATIVE_APPARENT_TEMP, ATTR_FORECAST_NATIVE_PRECIPITATION as ATTR_FORECAST_NATIVE_PRECIPITATION, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_TEMP_LOW as ATTR_FORECAST_NATIVE_TEMP_LOW, ATTR_FORECAST_NATIVE_WIND_GUST_SPEED as ATTR_FORECAST_NATIVE_WIND_GUST_SPEED, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_PRECIPITATION_PROBABILITY as ATTR_FORECAST_PRECIPITATION_PROBABILITY, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, ATTR_FORECAST_UV_INDEX as ATTR_FORECAST_UV_INDEX, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, CoordinatorWeatherEntity as CoordinatorWeatherEntity, Forecast as Forecast, WeatherEntityFeature as WeatherEntityFeature
from homeassistant.const import UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherEntity(CoordinatorWeatherEntity[AccuWeatherObservationDataUpdateCoordinator, AccuWeatherDailyForecastDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_native_precipitation_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_native_temperature_unit: Incomplete
    _attr_native_visibility_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_unique_id: Incomplete
    _attr_attribution: Incomplete
    _attr_device_info: Incomplete
    _attr_supported_features: Incomplete
    observation_coordinator: Incomplete
    daily_coordinator: Incomplete
    def __init__(self, accuweather_data: AccuWeatherData) -> None: ...
    @property
    def condition(self) -> str | None: ...
    @property
    def cloud_coverage(self) -> float: ...
    @property
    def native_apparent_temperature(self) -> float: ...
    @property
    def native_temperature(self) -> float: ...
    @property
    def native_pressure(self) -> float: ...
    @property
    def native_dew_point(self) -> float: ...
    @property
    def humidity(self) -> int: ...
    @property
    def native_wind_gust_speed(self) -> float: ...
    @property
    def native_wind_speed(self) -> float: ...
    @property
    def wind_bearing(self) -> int: ...
    @property
    def native_visibility(self) -> float: ...
    @property
    def uv_index(self) -> float: ...
    @callback
    def _async_forecast_daily(self) -> list[Forecast] | None: ...
