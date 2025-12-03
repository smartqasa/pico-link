from ..const import DOMAIN as DOMAIN
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import UnitOfTemperature as UnitOfTemperature

OVERKIZ_TO_HVAC_MODES: dict[str, HVACMode]
HVAC_MODES_TO_OVERKIZ: Incomplete

class AtlanticPassAPCHeatPumpMainComponent(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
