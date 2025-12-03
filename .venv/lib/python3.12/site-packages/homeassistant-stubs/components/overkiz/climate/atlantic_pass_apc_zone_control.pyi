from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import UnitOfTemperature as UnitOfTemperature

OVERKIZ_TO_HVAC_MODE: dict[str, HVACMode]
HVAC_MODE_TO_OVERKIZ: Incomplete

class AtlanticPassAPCZoneControl(OverkizEntity, ClimateEntity):
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def is_auto_hvac_mode_available(self) -> bool: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
