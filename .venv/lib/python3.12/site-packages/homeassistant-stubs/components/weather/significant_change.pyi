from .const import ATTR_WEATHER_APPARENT_TEMPERATURE as ATTR_WEATHER_APPARENT_TEMPERATURE, ATTR_WEATHER_CLOUD_COVERAGE as ATTR_WEATHER_CLOUD_COVERAGE, ATTR_WEATHER_DEW_POINT as ATTR_WEATHER_DEW_POINT, ATTR_WEATHER_HUMIDITY as ATTR_WEATHER_HUMIDITY, ATTR_WEATHER_OZONE as ATTR_WEATHER_OZONE, ATTR_WEATHER_PRESSURE as ATTR_WEATHER_PRESSURE, ATTR_WEATHER_PRESSURE_UNIT as ATTR_WEATHER_PRESSURE_UNIT, ATTR_WEATHER_TEMPERATURE as ATTR_WEATHER_TEMPERATURE, ATTR_WEATHER_TEMPERATURE_UNIT as ATTR_WEATHER_TEMPERATURE_UNIT, ATTR_WEATHER_UV_INDEX as ATTR_WEATHER_UV_INDEX, ATTR_WEATHER_VISIBILITY as ATTR_WEATHER_VISIBILITY, ATTR_WEATHER_WIND_BEARING as ATTR_WEATHER_WIND_BEARING, ATTR_WEATHER_WIND_GUST_SPEED as ATTR_WEATHER_WIND_GUST_SPEED, ATTR_WEATHER_WIND_SPEED as ATTR_WEATHER_WIND_SPEED, ATTR_WEATHER_WIND_SPEED_UNIT as ATTR_WEATHER_WIND_SPEED_UNIT
from homeassistant.const import UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_valid_float as check_valid_float
from typing import Any

SIGNIFICANT_ATTRIBUTES: set[str]
VALID_CARDINAL_DIRECTIONS: list[str]

def _cardinal_to_degrees(value: str | float | None) -> int | float | None: ...
@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
