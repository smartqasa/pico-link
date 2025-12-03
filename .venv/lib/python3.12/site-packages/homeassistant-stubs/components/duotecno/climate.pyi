from .const import DOMAIN as DOMAIN
from .entity import DuotecnoEntity as DuotecnoEntity, api_call as api_call
from _typeshed import Incomplete
from duotecno.controller import PyDuotecno as PyDuotecno
from duotecno.unit import SensUnit as SensUnit
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

HVACMODE: Final[Incomplete]
HVACMODE_REVERSE: Final[Incomplete]
PRESETMODES: Final[Incomplete]
PRESETMODES_REVERSE: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DuotecnoClimate(DuotecnoEntity, ClimateEntity):
    _unit: SensUnit
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_translation_key: str
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def preset_mode(self) -> str: ...
    @api_call
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @api_call
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
