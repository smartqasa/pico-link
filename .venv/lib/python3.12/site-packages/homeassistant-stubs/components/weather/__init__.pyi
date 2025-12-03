import abc
from .const import ATTR_WEATHER_APPARENT_TEMPERATURE as ATTR_WEATHER_APPARENT_TEMPERATURE, ATTR_WEATHER_CLOUD_COVERAGE as ATTR_WEATHER_CLOUD_COVERAGE, ATTR_WEATHER_DEW_POINT as ATTR_WEATHER_DEW_POINT, ATTR_WEATHER_HUMIDITY as ATTR_WEATHER_HUMIDITY, ATTR_WEATHER_OZONE as ATTR_WEATHER_OZONE, ATTR_WEATHER_PRECIPITATION_UNIT as ATTR_WEATHER_PRECIPITATION_UNIT, ATTR_WEATHER_PRESSURE as ATTR_WEATHER_PRESSURE, ATTR_WEATHER_PRESSURE_UNIT as ATTR_WEATHER_PRESSURE_UNIT, ATTR_WEATHER_TEMPERATURE as ATTR_WEATHER_TEMPERATURE, ATTR_WEATHER_TEMPERATURE_UNIT as ATTR_WEATHER_TEMPERATURE_UNIT, ATTR_WEATHER_UV_INDEX as ATTR_WEATHER_UV_INDEX, ATTR_WEATHER_VISIBILITY as ATTR_WEATHER_VISIBILITY, ATTR_WEATHER_VISIBILITY_UNIT as ATTR_WEATHER_VISIBILITY_UNIT, ATTR_WEATHER_WIND_BEARING as ATTR_WEATHER_WIND_BEARING, ATTR_WEATHER_WIND_GUST_SPEED as ATTR_WEATHER_WIND_GUST_SPEED, ATTR_WEATHER_WIND_SPEED as ATTR_WEATHER_WIND_SPEED, ATTR_WEATHER_WIND_SPEED_UNIT as ATTR_WEATHER_WIND_SPEED_UNIT, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, INTENT_GET_WEATHER as INTENT_GET_WEATHER, UNIT_CONVERSIONS as UNIT_CONVERSIONS, VALID_UNITS as VALID_UNITS, WeatherEntityFeature as WeatherEntityFeature
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import ABCCachedProperties as ABCCachedProperties, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.json import JsonValueType as JsonValueType
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM
from propcache import cached_property
from typing import Any, Final, Generic, Literal, Required, TypedDict, final
from typing_extensions import TypeVar

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_CONDITION_CLASS: str
ATTR_CONDITION_CLEAR_NIGHT: str
ATTR_CONDITION_CLOUDY: str
ATTR_CONDITION_EXCEPTIONAL: str
ATTR_CONDITION_FOG: str
ATTR_CONDITION_HAIL: str
ATTR_CONDITION_LIGHTNING: str
ATTR_CONDITION_LIGHTNING_RAINY: str
ATTR_CONDITION_PARTLYCLOUDY: str
ATTR_CONDITION_POURING: str
ATTR_CONDITION_RAINY: str
ATTR_CONDITION_SNOWY: str
ATTR_CONDITION_SNOWY_RAINY: str
ATTR_CONDITION_SUNNY: str
ATTR_CONDITION_WINDY: str
ATTR_CONDITION_WINDY_VARIANT: str
ATTR_FORECAST_IS_DAYTIME: Final[str]
ATTR_FORECAST_CONDITION: Final[str]
ATTR_FORECAST_HUMIDITY: Final[str]
ATTR_FORECAST_NATIVE_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION_PROBABILITY: Final[str]
ATTR_FORECAST_NATIVE_PRESSURE: Final[str]
ATTR_FORECAST_PRESSURE: Final[str]
ATTR_FORECAST_NATIVE_APPARENT_TEMP: Final[str]
ATTR_FORECAST_APPARENT_TEMP: Final[str]
ATTR_FORECAST_NATIVE_TEMP: Final[str]
ATTR_FORECAST_TEMP: Final[str]
ATTR_FORECAST_NATIVE_TEMP_LOW: Final[str]
ATTR_FORECAST_TEMP_LOW: Final[str]
ATTR_FORECAST_TIME: Final[str]
ATTR_FORECAST_WIND_BEARING: Final[str]
ATTR_FORECAST_NATIVE_WIND_GUST_SPEED: Final[str]
ATTR_FORECAST_WIND_GUST_SPEED: Final[str]
ATTR_FORECAST_NATIVE_WIND_SPEED: Final[str]
ATTR_FORECAST_WIND_SPEED: Final[str]
ATTR_FORECAST_NATIVE_DEW_POINT: Final[str]
ATTR_FORECAST_DEW_POINT: Final[str]
ATTR_FORECAST_CLOUD_COVERAGE: Final[str]
ATTR_FORECAST_UV_INDEX: Final[str]
ROUNDING_PRECISION: int
SERVICE_GET_FORECASTS: Final[str]
_ObservationUpdateCoordinatorT = TypeVar('_ObservationUpdateCoordinatorT', bound=DataUpdateCoordinator[Any], default=DataUpdateCoordinator[dict[str, Any]])
_DailyForecastUpdateCoordinatorT = TypeVar('_DailyForecastUpdateCoordinatorT', bound=TimestampDataUpdateCoordinator[Any], default=TimestampDataUpdateCoordinator[None])
_HourlyForecastUpdateCoordinatorT = TypeVar('_HourlyForecastUpdateCoordinatorT', bound=TimestampDataUpdateCoordinator[Any], default=_DailyForecastUpdateCoordinatorT)
_TwiceDailyForecastUpdateCoordinatorT = TypeVar('_TwiceDailyForecastUpdateCoordinatorT', bound=TimestampDataUpdateCoordinator[Any], default=_DailyForecastUpdateCoordinatorT)

def round_temperature(temperature: float | None, precision: float) -> float | None: ...

class Forecast(TypedDict, total=False):
    condition: str | None
    datetime: Required[str]
    humidity: float | None
    precipitation_probability: int | None
    cloud_coverage: int | None
    native_precipitation: float | None
    precipitation: None
    native_pressure: float | None
    pressure: None
    native_temperature: float | None
    temperature: None
    native_templow: float | None
    templow: None
    native_apparent_temperature: float | None
    wind_bearing: float | str | None
    native_wind_gust_speed: float | None
    native_wind_speed: float | None
    wind_speed: None
    native_dew_point: float | None
    uv_index: float | None
    is_daytime: bool | None

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WeatherEntityDescription(EntityDescription, frozen_or_thawed=True): ...

class PostInitMeta(ABCCachedProperties):
    def __call__(cls, *args: Any, **kwargs: Any) -> Any: ...

class PostInit(metaclass=PostInitMeta):
    @abc.abstractmethod
    def __post_init__(self, *args: Any, **kwargs: Any) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class WeatherEntity(Entity, PostInit, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: WeatherEntityDescription
    _attr_condition: str | None
    _attr_humidity: float | None
    _attr_ozone: float | None
    _attr_cloud_coverage: int | None
    _attr_uv_index: float | None
    _attr_precision: float
    _attr_state: None
    _attr_wind_bearing: float | str | None
    _attr_native_pressure: float | None
    _attr_native_pressure_unit: str | None
    _attr_native_apparent_temperature: float | None
    _attr_native_temperature: float | None
    _attr_native_temperature_unit: str | None
    _attr_native_visibility: float | None
    _attr_native_visibility_unit: str | None
    _attr_native_precipitation_unit: str | None
    _attr_native_wind_gust_speed: float | None
    _attr_native_wind_speed: float | None
    _attr_native_wind_speed_unit: str | None
    _attr_native_dew_point: float | None
    _forecast_listeners: dict[Literal['daily', 'hourly', 'twice_daily'], list[Callable[[list[JsonValueType] | None], None]]]
    _weather_option_temperature_unit: str | None
    _weather_option_pressure_unit: str | None
    _weather_option_visibility_unit: str | None
    _weather_option_precipitation_unit: str | None
    _weather_option_wind_speed_unit: str | None
    def __post_init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @cached_property
    def native_apparent_temperature(self) -> float | None: ...
    @cached_property
    def native_temperature(self) -> float | None: ...
    @cached_property
    def native_temperature_unit(self) -> str | None: ...
    @cached_property
    def native_dew_point(self) -> float | None: ...
    @final
    @property
    def _default_temperature_unit(self) -> str: ...
    @final
    @property
    def _temperature_unit(self) -> str: ...
    @cached_property
    def native_pressure(self) -> float | None: ...
    @cached_property
    def native_pressure_unit(self) -> str | None: ...
    @final
    @property
    def _default_pressure_unit(self) -> str: ...
    @final
    @property
    def _pressure_unit(self) -> str: ...
    @cached_property
    def humidity(self) -> float | None: ...
    @cached_property
    def native_wind_gust_speed(self) -> float | None: ...
    @cached_property
    def native_wind_speed(self) -> float | None: ...
    @cached_property
    def native_wind_speed_unit(self) -> str | None: ...
    @final
    @property
    def _default_wind_speed_unit(self) -> str: ...
    @final
    @property
    def _wind_speed_unit(self) -> str: ...
    @cached_property
    def wind_bearing(self) -> float | str | None: ...
    @cached_property
    def ozone(self) -> float | None: ...
    @cached_property
    def cloud_coverage(self) -> float | None: ...
    @cached_property
    def uv_index(self) -> float | None: ...
    @cached_property
    def native_visibility(self) -> float | None: ...
    @cached_property
    def native_visibility_unit(self) -> str | None: ...
    @final
    @property
    def _default_visibility_unit(self) -> str: ...
    @final
    @property
    def _visibility_unit(self) -> str: ...
    async def async_forecast_daily(self) -> list[Forecast] | None: ...
    async def async_forecast_twice_daily(self) -> list[Forecast] | None: ...
    async def async_forecast_hourly(self) -> list[Forecast] | None: ...
    @cached_property
    def native_precipitation_unit(self) -> str | None: ...
    @final
    @property
    def _default_precipitation_unit(self) -> str: ...
    @final
    @property
    def _precipitation_unit(self) -> str: ...
    @property
    def precision(self) -> float: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @final
    def _convert_forecast(self, native_forecast_list: list[Forecast]) -> list[JsonValueType]: ...
    @property
    @final
    def state(self) -> str | None: ...
    @cached_property
    def condition(self) -> str | None: ...
    @callback
    def async_registry_entry_updated(self) -> None: ...
    @callback
    def _async_subscription_started(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    @callback
    def _async_subscription_ended(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    @final
    @callback
    def async_subscribe_forecast(self, forecast_type: Literal['daily', 'hourly', 'twice_daily'], forecast_listener: Callable[[list[JsonValueType] | None], None]) -> CALLBACK_TYPE: ...
    @final
    async def async_update_listeners(self, forecast_types: Iterable[Literal['daily', 'hourly', 'twice_daily']] | None) -> None: ...

def raise_unsupported_forecast(entity_id: str, forecast_type: str) -> None: ...
async def async_get_forecasts_service(weather: WeatherEntity, service_call: ServiceCall) -> ServiceResponse: ...

class CoordinatorWeatherEntity(CoordinatorEntity[_ObservationUpdateCoordinatorT], WeatherEntity, Generic[_ObservationUpdateCoordinatorT, _DailyForecastUpdateCoordinatorT, _HourlyForecastUpdateCoordinatorT, _TwiceDailyForecastUpdateCoordinatorT]):
    forecast_coordinators: Incomplete
    forecast_valid: Incomplete
    unsub_forecast: dict[str, Callable[[], None] | None]
    def __init__(self, observation_coordinator: _ObservationUpdateCoordinatorT, *, context: Any = None, daily_coordinator: _DailyForecastUpdateCoordinatorT | None = None, hourly_coordinator: _HourlyForecastUpdateCoordinatorT | None = None, twice_daily_coordinator: _TwiceDailyForecastUpdateCoordinatorT | None = None, daily_forecast_valid: timedelta | None = None, hourly_forecast_valid: timedelta | None = None, twice_daily_forecast_valid: timedelta | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _remove_forecast_listener(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    @callback
    def _async_subscription_started(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    @callback
    def _handle_daily_forecast_coordinator_update(self) -> None: ...
    @callback
    def _handle_hourly_forecast_coordinator_update(self) -> None: ...
    @callback
    def _handle_twice_daily_forecast_coordinator_update(self) -> None: ...
    @final
    @callback
    def _handle_forecast_update(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    @callback
    def _async_subscription_ended(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    @final
    async def _async_refresh_forecast(self, coordinator: TimestampDataUpdateCoordinator[Any], forecast_valid_time: timedelta | None) -> bool: ...
    @callback
    def _async_forecast_daily(self) -> list[Forecast] | None: ...
    @callback
    def _async_forecast_hourly(self) -> list[Forecast] | None: ...
    @callback
    def _async_forecast_twice_daily(self) -> list[Forecast] | None: ...
    @final
    async def _async_forecast(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> list[Forecast] | None: ...
    @final
    async def async_forecast_daily(self) -> list[Forecast] | None: ...
    @final
    async def async_forecast_hourly(self) -> list[Forecast] | None: ...
    @final
    async def async_forecast_twice_daily(self) -> list[Forecast] | None: ...

class SingleCoordinatorWeatherEntity(CoordinatorWeatherEntity[_ObservationUpdateCoordinatorT, TimestampDataUpdateCoordinator[None]]):
    def __init__(self, coordinator: _ObservationUpdateCoordinatorT, context: Any = None) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
