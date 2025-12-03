import aiohttp
from .const import ATTR_SMHI_THUNDER_PROBABILITY as ATTR_SMHI_THUNDER_PROBABILITY, DOMAIN as DOMAIN, ENTITY_ID_SENSOR_FORMAT as ENTITY_ID_SENSOR_FORMAT
from _typeshed import Incomplete
from collections.abc import Mapping
from datetime import datetime
from homeassistant.components.weather import ATTR_CONDITION_CLEAR_NIGHT as ATTR_CONDITION_CLEAR_NIGHT, ATTR_CONDITION_CLOUDY as ATTR_CONDITION_CLOUDY, ATTR_CONDITION_EXCEPTIONAL as ATTR_CONDITION_EXCEPTIONAL, ATTR_CONDITION_FOG as ATTR_CONDITION_FOG, ATTR_CONDITION_HAIL as ATTR_CONDITION_HAIL, ATTR_CONDITION_LIGHTNING as ATTR_CONDITION_LIGHTNING, ATTR_CONDITION_LIGHTNING_RAINY as ATTR_CONDITION_LIGHTNING_RAINY, ATTR_CONDITION_PARTLYCLOUDY as ATTR_CONDITION_PARTLYCLOUDY, ATTR_CONDITION_POURING as ATTR_CONDITION_POURING, ATTR_CONDITION_RAINY as ATTR_CONDITION_RAINY, ATTR_CONDITION_SNOWY as ATTR_CONDITION_SNOWY, ATTR_CONDITION_SNOWY_RAINY as ATTR_CONDITION_SNOWY_RAINY, ATTR_CONDITION_SUNNY as ATTR_CONDITION_SUNNY, ATTR_CONDITION_WINDY as ATTR_CONDITION_WINDY, ATTR_CONDITION_WINDY_VARIANT as ATTR_CONDITION_WINDY_VARIANT, ATTR_FORECAST_CLOUD_COVERAGE as ATTR_FORECAST_CLOUD_COVERAGE, ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_HUMIDITY as ATTR_FORECAST_HUMIDITY, ATTR_FORECAST_NATIVE_PRECIPITATION as ATTR_FORECAST_NATIVE_PRECIPITATION, ATTR_FORECAST_NATIVE_PRESSURE as ATTR_FORECAST_NATIVE_PRESSURE, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_TEMP_LOW as ATTR_FORECAST_NATIVE_TEMP_LOW, ATTR_FORECAST_NATIVE_WIND_GUST_SPEED as ATTR_FORECAST_NATIVE_WIND_GUST_SPEED, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, Forecast as Forecast, WeatherEntity as WeatherEntity, WeatherEntityFeature as WeatherEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client, sun as sun
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util import Throttle as Throttle, slugify as slugify
from smhi.smhi_lib import SmhiForecast as SmhiForecast
from typing import Any, Final

_LOGGER: Incomplete
CONDITION_CLASSES: Final[dict[str, list[int]]]
CONDITION_MAP: Incomplete
TIMEOUT: int
RETRY_TIMEOUT: Incomplete
MIN_TIME_BETWEEN_UPDATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmhiWeather(WeatherEntity):
    _attr_attribution: str
    _attr_native_temperature_unit: Incomplete
    _attr_native_visibility_unit: Incomplete
    _attr_native_precipitation_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _forecast_daily: list[SmhiForecast] | None
    _forecast_hourly: list[SmhiForecast] | None
    _fail_count: int
    _smhi_api: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, latitude: str, longitude: str, session: aiohttp.ClientSession) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    _attr_native_temperature: Incomplete
    _attr_humidity: Incomplete
    _attr_native_wind_speed: Incomplete
    _attr_wind_bearing: Incomplete
    _attr_native_visibility: Incomplete
    _attr_native_pressure: Incomplete
    _attr_native_wind_gust_speed: Incomplete
    _attr_cloud_coverage: Incomplete
    _attr_condition: Incomplete
    async def async_update(self) -> None: ...
    async def retry_update(self, _: datetime) -> None: ...
    def _get_forecast_data(self, forecast_data: list[SmhiForecast] | None) -> list[Forecast] | None: ...
    async def async_forecast_daily(self) -> list[Forecast] | None: ...
    async def async_forecast_hourly(self) -> list[Forecast] | None: ...
