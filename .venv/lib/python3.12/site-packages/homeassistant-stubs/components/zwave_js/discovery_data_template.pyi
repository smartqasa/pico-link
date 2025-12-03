from .const import ENTITY_DESC_KEY_BATTERY as ENTITY_DESC_KEY_BATTERY, ENTITY_DESC_KEY_CO as ENTITY_DESC_KEY_CO, ENTITY_DESC_KEY_CO2 as ENTITY_DESC_KEY_CO2, ENTITY_DESC_KEY_CURRENT as ENTITY_DESC_KEY_CURRENT, ENTITY_DESC_KEY_ENERGY_MEASUREMENT as ENTITY_DESC_KEY_ENERGY_MEASUREMENT, ENTITY_DESC_KEY_ENERGY_PRODUCTION_POWER as ENTITY_DESC_KEY_ENERGY_PRODUCTION_POWER, ENTITY_DESC_KEY_ENERGY_PRODUCTION_TIME as ENTITY_DESC_KEY_ENERGY_PRODUCTION_TIME, ENTITY_DESC_KEY_ENERGY_PRODUCTION_TODAY as ENTITY_DESC_KEY_ENERGY_PRODUCTION_TODAY, ENTITY_DESC_KEY_ENERGY_PRODUCTION_TOTAL as ENTITY_DESC_KEY_ENERGY_PRODUCTION_TOTAL, ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING as ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING, ENTITY_DESC_KEY_HUMIDITY as ENTITY_DESC_KEY_HUMIDITY, ENTITY_DESC_KEY_ILLUMINANCE as ENTITY_DESC_KEY_ILLUMINANCE, ENTITY_DESC_KEY_MEASUREMENT as ENTITY_DESC_KEY_MEASUREMENT, ENTITY_DESC_KEY_POWER as ENTITY_DESC_KEY_POWER, ENTITY_DESC_KEY_POWER_FACTOR as ENTITY_DESC_KEY_POWER_FACTOR, ENTITY_DESC_KEY_PRESSURE as ENTITY_DESC_KEY_PRESSURE, ENTITY_DESC_KEY_SIGNAL_STRENGTH as ENTITY_DESC_KEY_SIGNAL_STRENGTH, ENTITY_DESC_KEY_TARGET_TEMPERATURE as ENTITY_DESC_KEY_TARGET_TEMPERATURE, ENTITY_DESC_KEY_TEMPERATURE as ENTITY_DESC_KEY_TEMPERATURE, ENTITY_DESC_KEY_TOTAL_INCREASING as ENTITY_DESC_KEY_TOTAL_INCREASING, ENTITY_DESC_KEY_UV_INDEX as ENTITY_DESC_KEY_UV_INDEX, ENTITY_DESC_KEY_VOLTAGE as ENTITY_DESC_KEY_VOLTAGE
from .helpers import ZwaveValueID as ZwaveValueID
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from enum import Enum as Enum
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UV_INDEX as UV_INDEX, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from typing import Any
from zwave_js_server.const.command_class.energy_production import EnergyProductionParameter, EnergyProductionScaleType as EnergyProductionScaleType
from zwave_js_server.const.command_class.meter import MeterScaleType as MeterScaleType
from zwave_js_server.const.command_class.multilevel_sensor import MultilevelSensorScaleType as MultilevelSensorScaleType, MultilevelSensorType
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import ConfigurationValue as ZwaveConfigurationValue, Value as ZwaveValue

ENERGY_PRODUCTION_DEVICE_CLASS_MAP: dict[str, list[EnergyProductionParameter]]
METER_DEVICE_CLASS_MAP: dict[str, list[MeterScaleType]]
MULTILEVEL_SENSOR_DEVICE_CLASS_MAP: dict[str, list[MultilevelSensorType]]
ENERGY_PRODUCTION_UNIT_MAP: dict[str, list[EnergyProductionScaleType]]
METER_UNIT_MAP: dict[str, list[MeterScaleType]]
MULTILEVEL_SENSOR_UNIT_MAP: dict[str, list[MultilevelSensorScaleType]]
_LOGGER: Incomplete

@dataclass
class BaseDiscoverySchemaDataTemplate:
    static_data: Any | None = ...
    def resolve_data(self, value: ZwaveValue) -> Any: ...
    def values_to_watch(self, resolved_data: Any) -> Iterable[ZwaveValue | None]: ...
    def value_ids_to_watch(self, resolved_data: Any) -> set[str]: ...
    @staticmethod
    def _get_value_from_id(node: ZwaveNode, value_id_obj: ZwaveValueID) -> ZwaveValue | ZwaveConfigurationValue | None: ...

@dataclass
class DynamicCurrentTempClimateDataTemplate(BaseDiscoverySchemaDataTemplate):
    lookup_table: dict[str | int, ZwaveValueID] = field(default_factory=dict)
    dependent_value: ZwaveValueID | None = ...
    def resolve_data(self, value: ZwaveValue) -> dict[str, Any]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue | None]: ...
    @staticmethod
    def current_temperature_value(resolved_data: dict[str, Any]) -> ZwaveValue | None: ...

@dataclass
class NumericSensorDataTemplateData:
    entity_description_key: str | None = ...
    unit_of_measurement: str | None = ...

class NumericSensorDataTemplate(BaseDiscoverySchemaDataTemplate):
    @staticmethod
    def find_key_from_matching_set[_T: Enum](enum_value: _T, set_map: Mapping[str, list[_T]]) -> str | None: ...
    def resolve_data(self, value: ZwaveValue) -> NumericSensorDataTemplateData: ...

@dataclass
class TiltValueMix:
    current_tilt_value_id: ZwaveValueID
    target_tilt_value_id: ZwaveValueID

@dataclass
class CoverTiltDataTemplate(BaseDiscoverySchemaDataTemplate, TiltValueMix):
    def resolve_data(self, value: ZwaveValue) -> dict[str, ZwaveValue]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue | None]: ...
    @staticmethod
    def current_tilt_value(resolved_data: dict[str, ZwaveValue]) -> ZwaveValue: ...
    @staticmethod
    def target_tilt_value(resolved_data: dict[str, ZwaveValue]) -> ZwaveValue: ...

@dataclass
class FanValueMapping:
    presets: dict[int, str] = field(default_factory=dict)
    speeds: list[tuple[int, int]] = field(default_factory=list)
    def __post_init__(self) -> None: ...

@dataclass
class FanValueMappingDataTemplate:
    def get_fan_value_mapping(self, resolved_data: dict[str, Any]) -> FanValueMapping | None: ...

@dataclass
class ConfigurableFanValueMappingValueMix:
    configuration_option: ZwaveValueID
    configuration_value_to_fan_value_mapping: dict[int, FanValueMapping]

@dataclass
class ConfigurableFanValueMappingDataTemplate(BaseDiscoverySchemaDataTemplate, FanValueMappingDataTemplate, ConfigurableFanValueMappingValueMix):
    def resolve_data(self, value: ZwaveValue) -> dict[str, ZwaveConfigurationValue | None]: ...
    def values_to_watch(self, resolved_data: dict[str, ZwaveConfigurationValue | None]) -> Iterable[ZwaveConfigurationValue | None]: ...
    def get_fan_value_mapping(self, resolved_data: dict[str, ZwaveConfigurationValue | None]) -> FanValueMapping | None: ...

@dataclass
class FixedFanValueMappingValueMix:
    fan_value_mapping: FanValueMapping

@dataclass
class FixedFanValueMappingDataTemplate(BaseDiscoverySchemaDataTemplate, FanValueMappingDataTemplate, FixedFanValueMappingValueMix):
    def get_fan_value_mapping(self, resolved_data: dict[str, ZwaveConfigurationValue]) -> FanValueMapping: ...
