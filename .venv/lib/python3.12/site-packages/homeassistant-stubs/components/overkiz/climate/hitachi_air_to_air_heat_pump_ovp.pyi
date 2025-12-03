from ..const import DOMAIN as DOMAIN
from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from typing import Any

PRESET_HOLIDAY_MODE: str
FAN_SILENT: str
TEMP_MIN: int
TEMP_MAX: int
TEMP_AUTO_MIN: int
TEMP_AUTO_MAX: int
AUTO_PIVOT_TEMPERATURE: int
AUTO_TEMPERATURE_CHANGE_MIN: Incomplete
AUTO_TEMPERATURE_CHANGE_MAX: Incomplete
OVERKIZ_TO_HVAC_MODES: dict[str, HVACMode]
HVAC_MODES_TO_OVERKIZ: dict[HVACMode, str]
OVERKIZ_TO_SWING_MODES: dict[str, str]
SWING_MODES_TO_OVERKIZ: Incomplete
OVERKIZ_TO_FAN_MODES: dict[str, str]
FAN_MODES_TO_OVERKIZ: dict[str, str]

class HitachiAirToAirHeatPumpOVP(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_fan_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_swing_modes: Incomplete
    _attr_target_temperature_step: float
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    _attr_supported_features: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def fan_mode(self) -> str | None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    @property
    def swing_mode(self) -> str | None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    @property
    def target_temperature(self) -> int | None: ...
    @property
    def current_temperature(self) -> int | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def auto_manu_mode(self) -> str | None: ...
    @property
    def temperature_change(self) -> int | None: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    def _control_backfill(self, value: str | None, state_name: str, fallback_value: str) -> str: ...
    async def _global_control(self, main_operation: str | None = None, target_temperature: int | None = None, fan_mode: str | None = None, hvac_mode: str | None = None, swing_mode: str | None = None, leave_home: str | None = None) -> None: ...
