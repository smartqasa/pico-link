from ..const import DOMAIN as DOMAIN
from ..entity import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator, OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from typing import Any

OVERKIZ_TO_HVAC_MODE: dict[str, HVACMode]
HVAC_MODE_TO_OVERKIZ: Incomplete
OVERKIZ_TO_PRESET_MODE: dict[str, str]
PRESET_MODE_TO_OVERKIZ: Incomplete

class HitachiAirToWaterHeatingZone(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_min_temp: float
    _attr_max_temp: float
    _attr_precision: float
    _attr_target_temperature_step: float
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
