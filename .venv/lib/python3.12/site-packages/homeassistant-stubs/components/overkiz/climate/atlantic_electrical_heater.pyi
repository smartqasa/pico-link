from ..const import DOMAIN as DOMAIN
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.const import UnitOfTemperature as UnitOfTemperature

PRESET_COMFORT1: str
PRESET_COMFORT2: str
PRESET_FROST_PROTECTION: str
OVERKIZ_TO_HVAC_MODES: dict[str, HVACMode]
HVAC_MODES_TO_OVERKIZ: Incomplete
OVERKIZ_TO_PRESET_MODES: dict[str, str]
PRESET_MODES_TO_OVERKIZ: Incomplete

class AtlanticElectricalHeater(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
