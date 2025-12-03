from . import WeatherEntity as WeatherEntity
from collections.abc import Callable as Callable
from enum import IntFlag
from homeassistant.const import UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter
from typing import Final

class WeatherEntityFeature(IntFlag):
    FORECAST_DAILY = 1
    FORECAST_HOURLY = 2
    FORECAST_TWICE_DAILY = 4

ATTR_WEATHER_HUMIDITY: str
ATTR_WEATHER_OZONE: str
ATTR_WEATHER_DEW_POINT: str
ATTR_WEATHER_PRESSURE: str
ATTR_WEATHER_PRESSURE_UNIT: str
ATTR_WEATHER_APPARENT_TEMPERATURE: str
ATTR_WEATHER_TEMPERATURE: str
ATTR_WEATHER_TEMPERATURE_UNIT: str
ATTR_WEATHER_VISIBILITY: str
ATTR_WEATHER_VISIBILITY_UNIT: str
ATTR_WEATHER_WIND_BEARING: str
ATTR_WEATHER_WIND_GUST_SPEED: str
ATTR_WEATHER_WIND_SPEED: str
ATTR_WEATHER_WIND_SPEED_UNIT: str
ATTR_WEATHER_PRECIPITATION_UNIT: str
ATTR_WEATHER_CLOUD_COVERAGE: str
ATTR_WEATHER_UV_INDEX: str
DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[WeatherEntity]]
INTENT_GET_WEATHER: str
VALID_UNITS_PRESSURE: set[str]
VALID_UNITS_TEMPERATURE: set[str]
VALID_UNITS_PRECIPITATION: set[str]
VALID_UNITS_VISIBILITY: set[str]
VALID_UNITS_WIND_SPEED: set[str]
UNIT_CONVERSIONS: dict[str, Callable[[float, str, str], float]]
VALID_UNITS: dict[str, set[str]]
