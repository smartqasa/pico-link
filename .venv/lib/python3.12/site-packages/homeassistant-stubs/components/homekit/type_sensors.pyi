from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_AIR_PARTICULATE_DENSITY as CHAR_AIR_PARTICULATE_DENSITY, CHAR_AIR_QUALITY as CHAR_AIR_QUALITY, CHAR_CARBON_DIOXIDE_DETECTED as CHAR_CARBON_DIOXIDE_DETECTED, CHAR_CARBON_DIOXIDE_LEVEL as CHAR_CARBON_DIOXIDE_LEVEL, CHAR_CARBON_DIOXIDE_PEAK_LEVEL as CHAR_CARBON_DIOXIDE_PEAK_LEVEL, CHAR_CARBON_MONOXIDE_DETECTED as CHAR_CARBON_MONOXIDE_DETECTED, CHAR_CARBON_MONOXIDE_LEVEL as CHAR_CARBON_MONOXIDE_LEVEL, CHAR_CARBON_MONOXIDE_PEAK_LEVEL as CHAR_CARBON_MONOXIDE_PEAK_LEVEL, CHAR_CONTACT_SENSOR_STATE as CHAR_CONTACT_SENSOR_STATE, CHAR_CURRENT_AMBIENT_LIGHT_LEVEL as CHAR_CURRENT_AMBIENT_LIGHT_LEVEL, CHAR_CURRENT_HUMIDITY as CHAR_CURRENT_HUMIDITY, CHAR_CURRENT_TEMPERATURE as CHAR_CURRENT_TEMPERATURE, CHAR_LEAK_DETECTED as CHAR_LEAK_DETECTED, CHAR_MOTION_DETECTED as CHAR_MOTION_DETECTED, CHAR_NITROGEN_DIOXIDE_DENSITY as CHAR_NITROGEN_DIOXIDE_DENSITY, CHAR_OCCUPANCY_DETECTED as CHAR_OCCUPANCY_DETECTED, CHAR_PM10_DENSITY as CHAR_PM10_DENSITY, CHAR_PM25_DENSITY as CHAR_PM25_DENSITY, CHAR_SMOKE_DETECTED as CHAR_SMOKE_DETECTED, CHAR_VOC_DENSITY as CHAR_VOC_DENSITY, CONF_THRESHOLD_CO as CONF_THRESHOLD_CO, CONF_THRESHOLD_CO2 as CONF_THRESHOLD_CO2, PROP_CELSIUS as PROP_CELSIUS, PROP_MAX_VALUE as PROP_MAX_VALUE, PROP_MIN_VALUE as PROP_MIN_VALUE, SERV_AIR_QUALITY_SENSOR as SERV_AIR_QUALITY_SENSOR, SERV_CARBON_DIOXIDE_SENSOR as SERV_CARBON_DIOXIDE_SENSOR, SERV_CARBON_MONOXIDE_SENSOR as SERV_CARBON_MONOXIDE_SENSOR, SERV_CONTACT_SENSOR as SERV_CONTACT_SENSOR, SERV_HUMIDITY_SENSOR as SERV_HUMIDITY_SENSOR, SERV_LEAK_SENSOR as SERV_LEAK_SENSOR, SERV_LIGHT_SENSOR as SERV_LIGHT_SENSOR, SERV_MOTION_SENSOR as SERV_MOTION_SENSOR, SERV_OCCUPANCY_SENSOR as SERV_OCCUPANCY_SENSOR, SERV_SMOKE_SENSOR as SERV_SMOKE_SENSOR, SERV_TEMPERATURE_SENSOR as SERV_TEMPERATURE_SENSOR, THRESHOLD_CO as THRESHOLD_CO, THRESHOLD_CO2 as THRESHOLD_CO2
from .util import convert_to_float as convert_to_float, density_to_air_quality as density_to_air_quality, density_to_air_quality_nitrogen_dioxide as density_to_air_quality_nitrogen_dioxide, density_to_air_quality_pm10 as density_to_air_quality_pm10, density_to_air_quality_voc as density_to_air_quality_voc, temperature_to_homekit as temperature_to_homekit
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, STATE_HOME as STATE_HOME, STATE_ON as STATE_ON, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import State as State, callback as callback
from pyhap.service import Service as Service
from typing import Any, NamedTuple

_LOGGER: Incomplete

class SI(NamedTuple):
    service: str
    char: str
    format: Callable[[bool], int | bool]

BINARY_SENSOR_SERVICE_MAP: dict[str, SI]

class TemperatureSensor(HomeAccessory):
    char_temp: Incomplete
    def __init__(self, *args: Any) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class HumiditySensor(HomeAccessory):
    char_humidity: Incomplete
    def __init__(self, *args: Any) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class AirQualitySensor(HomeAccessory):
    def __init__(self, *args: Any) -> None: ...
    char_quality: Incomplete
    char_density: Incomplete
    def create_services(self) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class PM10Sensor(AirQualitySensor):
    char_quality: Incomplete
    char_density: Incomplete
    def create_services(self) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class PM25Sensor(AirQualitySensor):
    char_quality: Incomplete
    char_density: Incomplete
    def create_services(self) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class NitrogenDioxideSensor(AirQualitySensor):
    char_quality: Incomplete
    char_density: Incomplete
    def create_services(self) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class VolatileOrganicCompoundsSensor(AirQualitySensor):
    char_quality: Incomplete
    char_density: Incomplete
    def create_services(self) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class CarbonMonoxideSensor(HomeAccessory):
    threshold_co: Incomplete
    char_level: Incomplete
    char_peak: Incomplete
    char_detected: Incomplete
    def __init__(self, *args: Any) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class CarbonDioxideSensor(HomeAccessory):
    threshold_co2: Incomplete
    char_level: Incomplete
    char_peak: Incomplete
    char_detected: Incomplete
    def __init__(self, *args: Any) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class LightSensor(HomeAccessory):
    char_light: Incomplete
    def __init__(self, *args: Any) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...

class BinarySensor(HomeAccessory):
    format: Incomplete
    char_detected: Incomplete
    def __init__(self, *args: Any) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...
