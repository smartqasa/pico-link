from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfApparentPower as UnitOfApparentPower, UnitOfArea as UnitOfArea, UnitOfBloodGlucoseConcentration as UnitOfBloodGlucoseConcentration, UnitOfConductivity as UnitOfConductivity, UnitOfDataRate as UnitOfDataRate, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfInformation as UnitOfInformation, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfReactivePower as UnitOfReactivePower, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.util.unit_conversion import BaseUnitConverter as BaseUnitConverter, TemperatureConverter as TemperatureConverter, VolumeFlowRateConverter as VolumeFlowRateConverter
from typing import Final

ATTR_VALUE: str
ATTR_MIN: str
ATTR_MAX: str
ATTR_STEP: str
ATTR_STEP_VALIDATION: str
DEFAULT_MIN_VALUE: float
DEFAULT_MAX_VALUE: float
DEFAULT_STEP: float
DOMAIN: str
SERVICE_SET_VALUE: str

class NumberMode(StrEnum):
    AUTO = 'auto'
    BOX = 'box'
    SLIDER = 'slider'

class NumberDeviceClass(StrEnum):
    APPARENT_POWER = 'apparent_power'
    AQI = 'aqi'
    AREA = 'area'
    ATMOSPHERIC_PRESSURE = 'atmospheric_pressure'
    BATTERY = 'battery'
    BLOOD_GLUCOSE_CONCENTRATION = 'blood_glucose_concentration'
    CO = 'carbon_monoxide'
    CO2 = 'carbon_dioxide'
    CONDUCTIVITY = 'conductivity'
    CURRENT = 'current'
    DATA_RATE = 'data_rate'
    DATA_SIZE = 'data_size'
    DISTANCE = 'distance'
    DURATION = 'duration'
    ENERGY = 'energy'
    ENERGY_STORAGE = 'energy_storage'
    FREQUENCY = 'frequency'
    GAS = 'gas'
    HUMIDITY = 'humidity'
    ILLUMINANCE = 'illuminance'
    IRRADIANCE = 'irradiance'
    MOISTURE = 'moisture'
    MONETARY = 'monetary'
    NITROGEN_DIOXIDE = 'nitrogen_dioxide'
    NITROGEN_MONOXIDE = 'nitrogen_monoxide'
    NITROUS_OXIDE = 'nitrous_oxide'
    OZONE = 'ozone'
    PH = 'ph'
    PM1 = 'pm1'
    PM10 = 'pm10'
    PM25 = 'pm25'
    POWER_FACTOR = 'power_factor'
    POWER = 'power'
    PRECIPITATION = 'precipitation'
    PRECIPITATION_INTENSITY = 'precipitation_intensity'
    PRESSURE = 'pressure'
    REACTIVE_POWER = 'reactive_power'
    SIGNAL_STRENGTH = 'signal_strength'
    SOUND_PRESSURE = 'sound_pressure'
    SPEED = 'speed'
    SULPHUR_DIOXIDE = 'sulphur_dioxide'
    TEMPERATURE = 'temperature'
    VOLATILE_ORGANIC_COMPOUNDS = 'volatile_organic_compounds'
    VOLATILE_ORGANIC_COMPOUNDS_PARTS = 'volatile_organic_compounds_parts'
    VOLTAGE = 'voltage'
    VOLUME = 'volume'
    VOLUME_STORAGE = 'volume_storage'
    VOLUME_FLOW_RATE = 'volume_flow_rate'
    WATER = 'water'
    WEIGHT = 'weight'
    WIND_SPEED = 'wind_speed'

DEVICE_CLASSES_SCHEMA: Final[Incomplete]
DEVICE_CLASS_UNITS: dict[NumberDeviceClass, set[type[StrEnum] | str | None]]
UNIT_CONVERTERS: dict[NumberDeviceClass, type[BaseUnitConverter]]
