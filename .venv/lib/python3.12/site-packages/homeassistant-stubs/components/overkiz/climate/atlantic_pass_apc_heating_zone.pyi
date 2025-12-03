from ..const import DOMAIN as DOMAIN
from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_HOME as PRESET_HOME, PRESET_SLEEP as PRESET_SLEEP
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from typing import Any

OVERKIZ_TO_HVAC_MODE: dict[str, HVACMode]
HVAC_MODE_TO_OVERKIZ: Incomplete
PRESET_EXTERNAL: str
PRESET_FROST_PROTECTION: str
OVERKIZ_TO_PRESET_MODES: dict[str, str]
PRESET_MODES_TO_OVERKIZ: dict[str, str]
OVERKIZ_TO_PROFILE_MODES: dict[str, str]
OVERKIZ_TEMPERATURE_STATE_BY_PROFILE: dict[str, str]

class AtlanticPassAPCHeatingZone(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    temperature_device: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def current_heating_profile(self) -> str: ...
    async def async_set_heating_mode(self, mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
