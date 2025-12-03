from ..const import DOMAIN as DOMAIN
from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE, UnitOfTemperature as UnitOfTemperature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from typing import Any

PRESET_MANUAL: str
PRESET_FROST_PROTECTION: str
OVERKIZ_TO_HVAC_ACTION: dict[str, HVACAction]
OVERKIZ_TO_PRESET_MODE: dict[str, str]
PRESET_MODE_TO_OVERKIZ: Incomplete
TEMPERATURE_SENSOR_DEVICE_INDEX: int

class ValveHeatingTemperatureInterface(OverkizEntity, ClimateEntity):
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    temperature_device: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def target_temperature(self) -> float: ...
    @property
    def current_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> str: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
