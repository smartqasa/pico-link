from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from enum import IntEnum
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityDescription as ClimateEntityDescription, ClimateEntityFeature as ClimateEntityFeature, DEFAULT_MAX_TEMP as DEFAULT_MAX_TEMP, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

TEMPERATURE_SCALING_FACTOR: int
HVAC_SYSTEM_MODE_MAP: Incomplete
SINGLE_SETPOINT_DEVICES: set[tuple[int, int]]
SUPPORT_DRY_MODE_DEVICES: set[tuple[int, int]]
SUPPORT_FAN_MODE_DEVICES: set[tuple[int, int]]
SystemModeEnum: Incomplete
ControlSequenceEnum: Incomplete
ThermostatFeature: Incomplete

class ThermostatRunningState(IntEnum):
    Heat = 1
    Cool = 2
    Fan = 4
    HeatStage2 = 8
    CoolStage2 = 16
    FanStage2 = 32
    FanStage3 = 64

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterClimate(MatterEntity, ClimateEntity):
    _attr_temperature_unit: str
    _attr_hvac_mode: HVACMode
    _feature_map: int | None
    _platform_translation_key: str
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_hvac_action: Incomplete
    _attr_target_temperature: Incomplete
    _attr_target_temperature_high: Incomplete
    _attr_target_temperature_low: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    _attr_hvac_modes: list[HVACMode]
    _attr_supported_features: Incomplete
    @callback
    def _calculate_features(self) -> None: ...
    @callback
    def _get_temperature_in_degrees(self, attribute: type[clusters.ClusterAttributeDescriptor]) -> float | None: ...

DISCOVERY_SCHEMAS: Incomplete
