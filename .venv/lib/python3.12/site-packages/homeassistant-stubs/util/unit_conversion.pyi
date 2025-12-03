from _typeshed import Incomplete
from collections.abc import Callable as Callable
from functools import lru_cache
from homeassistant.const import CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, UnitOfArea as UnitOfArea, UnitOfBloodGlucoseConcentration as UnitOfBloodGlucoseConcentration, UnitOfConductivity as UnitOfConductivity, UnitOfDataRate as UnitOfDataRate, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfInformation as UnitOfInformation, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_MM_TO_M: float
_CM_TO_M: float
_KM_TO_M: int
_IN_TO_M: float
_FOOT_TO_M: Incomplete
_YARD_TO_M: Incomplete
_MILE_TO_M: Incomplete
_NAUTICAL_MILE_TO_M: int
_CM2_TO_M2: Incomplete
_MM2_TO_M2: Incomplete
_KM2_TO_M2: Incomplete
_IN2_TO_M2: Incomplete
_FT2_TO_M2: Incomplete
_YD2_TO_M2: Incomplete
_MI2_TO_M2: Incomplete
_ACRE_TO_M2: Incomplete
_HECTARE_TO_M2: Incomplete
_MIN_TO_SEC: int
_HRS_TO_MINUTES: int
_HRS_TO_SECS: Incomplete
_DAYS_TO_SECS: Incomplete
_WH_TO_J: int
_WH_TO_CAL: Incomplete
_POUND_TO_G: float
_OUNCE_TO_G: Incomplete
_STONE_TO_G: Incomplete
_STANDARD_GRAVITY: float
_MERCURY_DENSITY: float
_L_TO_CUBIC_METER: float
_ML_TO_CUBIC_METER: Incomplete
_GALLON_TO_CUBIC_METER: Incomplete
_FLUID_OUNCE_TO_CUBIC_METER: Incomplete
_CUBIC_FOOT_TO_CUBIC_METER: Incomplete

class BaseUnitConverter:
    UNIT_CLASS: str
    VALID_UNITS: set[str | None]
    _UNIT_CONVERSION: dict[str | None, float]
    @classmethod
    def convert(cls, value: float, from_unit: str | None, to_unit: str | None) -> float: ...
    @classmethod
    @lru_cache
    def converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    def _get_from_to_ratio(cls, from_unit: str | None, to_unit: str | None) -> tuple[float, float]: ...
    @classmethod
    @lru_cache
    def converter_factory_allow_none(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float | None], float | None]: ...
    @classmethod
    @lru_cache
    def get_unit_ratio(cls, from_unit: str | None, to_unit: str | None) -> float: ...

class DataRateConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class AreaConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class DistanceConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class BloodGlucoseConcentrationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ConductivityConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ElectricCurrentConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ElectricPotentialConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class EnergyConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class InformationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class MassConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class PowerConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class PressureConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class SpeedConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete
    @classmethod
    @lru_cache
    def converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    @lru_cache
    def converter_factory_allow_none(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float | None], float | None]: ...
    @classmethod
    def _converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    def _ms_to_beaufort(cls, ms: float) -> float: ...
    @classmethod
    def _beaufort_to_ms(cls, beaufort: float) -> float: ...

class TemperatureConverter(BaseUnitConverter):
    UNIT_CLASS: str
    VALID_UNITS: Incomplete
    _UNIT_CONVERSION: Incomplete
    @classmethod
    @lru_cache
    def converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    @lru_cache
    def converter_factory_allow_none(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float | None], float | None]: ...
    @classmethod
    def _converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    def convert_interval(cls, interval: float, from_unit: str, to_unit: str) -> float: ...
    @classmethod
    def _kelvin_to_fahrenheit(cls, kelvin: float) -> float: ...
    @classmethod
    def _fahrenheit_to_kelvin(cls, fahrenheit: float) -> float: ...
    @classmethod
    def _fahrenheit_to_celsius(cls, fahrenheit: float) -> float: ...
    @classmethod
    def _kelvin_to_celsius(cls, kelvin: float) -> float: ...
    @classmethod
    def _celsius_to_fahrenheit(cls, celsius: float) -> float: ...
    @classmethod
    def _celsius_to_kelvin(cls, celsius: float) -> float: ...

class UnitlessRatioConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class VolumeConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class VolumeFlowRateConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class DurationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete
