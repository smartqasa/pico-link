from .unit_conversion import AreaConverter as AreaConverter, DistanceConverter as DistanceConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter, VolumeConverter as VolumeConverter
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import ACCUMULATED_PRECIPITATION as ACCUMULATED_PRECIPITATION, AREA as AREA, LENGTH as LENGTH, MASS as MASS, PRESSURE as PRESSURE, TEMPERATURE as TEMPERATURE, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, UnitOfArea as UnitOfArea, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume, UnitOfVolumetricFlux as UnitOfVolumetricFlux, VOLUME as VOLUME, WIND_SPEED as WIND_SPEED
from typing import Final

_CONF_UNIT_SYSTEM_IMPERIAL: Final[str]
_CONF_UNIT_SYSTEM_METRIC: Final[str]
_CONF_UNIT_SYSTEM_US_CUSTOMARY: Final[str]
AREA_UNITS: Incomplete
LENGTH_UNITS: Incomplete
MASS_UNITS: set[str]
PRESSURE_UNITS: Incomplete
VOLUME_UNITS: Incomplete
WIND_SPEED_UNITS: Incomplete
TEMPERATURE_UNITS: set[str]
_VALID_BY_TYPE: dict[str, set[str] | set[str | None]]

def _is_valid_unit(unit: str, unit_type: str) -> bool: ...

class UnitSystem:
    _name: Incomplete
    accumulated_precipitation_unit: Incomplete
    area_unit: Incomplete
    length_unit: Incomplete
    mass_unit: Incomplete
    pressure_unit: Incomplete
    temperature_unit: Incomplete
    volume_unit: Incomplete
    wind_speed_unit: Incomplete
    _conversions: Incomplete
    def __init__(self, name: str, *, accumulated_precipitation: UnitOfPrecipitationDepth, area: UnitOfArea, conversions: dict[tuple[SensorDeviceClass | str | None, str | None], str], length: UnitOfLength, mass: UnitOfMass, pressure: UnitOfPressure, temperature: UnitOfTemperature, volume: UnitOfVolume, wind_speed: UnitOfSpeed) -> None: ...
    def temperature(self, temperature: float, from_unit: str) -> float: ...
    def length(self, length: float | None, from_unit: str) -> float: ...
    def accumulated_precipitation(self, precip: float | None, from_unit: str) -> float: ...
    def area(self, area: float | None, from_unit: str) -> float: ...
    def pressure(self, pressure: float | None, from_unit: str) -> float: ...
    def wind_speed(self, wind_speed: float | None, from_unit: str) -> float: ...
    def volume(self, volume: float | None, from_unit: str) -> float: ...
    def as_dict(self) -> dict[str, str]: ...
    def get_converted_unit(self, device_class: SensorDeviceClass | str | None, original_unit: str | None) -> str | None: ...

def get_unit_system(key: str) -> UnitSystem: ...
def _deprecated_unit_system(value: str) -> str: ...

validate_unit_system: Incomplete
METRIC_SYSTEM: Incomplete
US_CUSTOMARY_SYSTEM: Incomplete
IMPERIAL_SYSTEM = US_CUSTOMARY_SYSTEM
