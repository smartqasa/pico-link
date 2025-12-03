from ..const import DOMAIN as DOMAIN
from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, HVACMode as HVACMode
from homeassistant.const import UnitOfTemperature as UnitOfTemperature

FAN_BOOST: str
FAN_KITCHEN: str
FAN_AWAY: str
FAN_BYPASS: str
PRESET_AUTO: str
PRESET_PROG: str
PRESET_MANUAL: str
OVERKIZ_TO_FAN_MODES: dict[str, str]
FAN_MODES_TO_OVERKIZ: Incomplete
TEMPERATURE_SENSOR_DEVICE_INDEX: int

class AtlanticHeatRecoveryVentilation(OverkizEntity, ClimateEntity):
    _attr_fan_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_translation_key = DOMAIN
    temperature_device: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def fan_mode(self) -> str | None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def _set_ventilation_mode(self, cooling: str | None = None, prog: str | None = None) -> None: ...
