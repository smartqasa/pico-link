from ..const import DOMAIN as DOMAIN
from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from typing import Any

PRESET_AUTO: str
PRESET_COMFORT1: str
PRESET_COMFORT2: str
PRESET_FROST_PROTECTION: str
PRESET_PROG: str
PRESET_EXTERNAL: str
OVERKIZ_TO_PRESET_MODE: dict[str, str]
PRESET_MODE_TO_OVERKIZ: Incomplete
OVERKIZ_TO_HVAC_MODE: dict[str, HVACMode]
HVAC_MODE_TO_OVERKIZ: Incomplete
TEMPERATURE_SENSOR_DEVICE_INDEX: int

class AtlanticElectricalHeaterWithAdjustableTemperatureSetpoint(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_translation_key = DOMAIN
    temperature_device: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
