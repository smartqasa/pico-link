from . import Eq3ConfigEntry as Eq3ConfigEntry
from .const import CurrentTemperatureSelector as CurrentTemperatureSelector, EQ_TO_HA_HVAC as EQ_TO_HA_HVAC, HA_TO_EQ_HVAC as HA_TO_EQ_HVAC, Preset as Preset, TargetTemperatureSelector as TargetTemperatureSelector
from .entity import Eq3Entity as Eq3Entity
from _typeshed import Incomplete
from eq3btsmart.const import EQ3BT_MAX_TEMP, EQ3BT_OFF_TEMP
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Eq3ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Eq3Climate(Eq3Entity, ClimateEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_min_temp = EQ3BT_OFF_TEMP
    _attr_max_temp = EQ3BT_MAX_TEMP
    _attr_precision = PRECISION_HALVES
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_should_poll: bool
    _attr_available: bool
    _attr_hvac_mode: HVACMode | None
    _attr_hvac_action: HVACAction | None
    _attr_preset_mode: str | None
    _target_temperature: float | None
    @callback
    def _async_on_updated(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    @callback
    def _async_on_status_updated(self) -> None: ...
    @callback
    def _async_on_device_updated(self) -> None: ...
    def _get_current_temperature(self) -> float | None: ...
    def _get_target_temperature(self) -> float | None: ...
    def _get_current_preset_mode(self) -> str: ...
    def _get_current_hvac_action(self) -> HVACAction: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
