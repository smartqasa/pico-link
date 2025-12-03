from . import BAFConfigEntry as BAFConfigEntry
from .entity import BAFEntity as BAFEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: BAFConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFAutoComfort(BAFEntity, ClimateEntity):
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_translation_key: str
    _attr_hvac_mode: Incomplete
    _attr_hvac_action: Incomplete
    _attr_target_temperature: Incomplete
    _attr_current_temperature: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
