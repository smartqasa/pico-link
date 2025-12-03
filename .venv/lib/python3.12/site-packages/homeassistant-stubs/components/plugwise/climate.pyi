from . import PlugwiseConfigEntry as PlugwiseConfigEntry
from .const import DOMAIN as DOMAIN, MASTER_THERMOSTATS as MASTER_THERMOSTATS
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseClimateEntity(PlugwiseEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    _previous_mode: str
    _attr_unique_id: Incomplete
    _devices: Incomplete
    _gateway: Incomplete
    _gateway_data: Incomplete
    _location: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_target_temperature_step: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str) -> None: ...
    def _previous_action_mode(self, coordinator: PlugwiseDataUpdateCoordinator) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float: ...
    @property
    def target_temperature_high(self) -> float: ...
    @property
    def target_temperature_low(self) -> float: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def preset_mode(self) -> str | None: ...
    @plugwise_command
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @plugwise_command
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @plugwise_command
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
