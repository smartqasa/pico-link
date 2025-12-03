from .device_info import NestDeviceInfo as NestDeviceInfo
from .types import NestConfigEntry as NestConfigEntry
from _typeshed import Incomplete
from google_nest_sdm.device import Device as Device
from google_nest_sdm.thermostat_traits import ThermostatEcoTrait, ThermostatTemperatureSetpointTrait
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

THERMOSTAT_MODE_MAP: dict[str, HVACMode]
THERMOSTAT_INV_MODE_MAP: Incomplete
THERMOSTAT_ECO_MODE: str
THERMOSTAT_HVAC_STATUS_MAP: Incomplete
THERMOSTAT_RANGE_MODES: Incomplete
PRESET_MODE_MAP: Incomplete
PRESET_INV_MODE_MAP: Incomplete
FAN_MODE_MAP: Incomplete
FAN_INV_MODE_MAP: Incomplete
FAN_INV_MODES: Incomplete
MAX_FAN_DURATION: int
MIN_TEMP: int
MAX_TEMP: int
MIN_TEMP_RANGE: float

async def async_setup_entry(hass: HomeAssistant, entry: NestConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ThermostatEntity(ClimateEntity):
    _attr_min_temp = MIN_TEMP
    _attr_max_temp = MAX_TEMP
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_name: Incomplete
    _device: Incomplete
    _device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    def __init__(self, device: Device) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_supported_features: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def target_temperature_high(self) -> float | None: ...
    @property
    def target_temperature_low(self) -> float | None: ...
    @property
    def _target_temperature_trait(self) -> ThermostatEcoTrait | ThermostatTemperatureSetpointTrait | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def preset_mode(self) -> str: ...
    @property
    def preset_modes(self) -> list[str]: ...
    @property
    def fan_mode(self) -> str: ...
    @property
    def fan_modes(self) -> list[str]: ...
    def _get_supported_features(self) -> ClimateEntityFeature: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
