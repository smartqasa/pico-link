from . import TPLinkConfigEntry as TPLinkConfigEntry
from .const import UNIT_MAPPING as UNIT_MAPPING
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import Device as Device
from typing import Any

STATE_TO_ACTION: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkClimateEntity(CoordinatedTPLinkEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_precision = PRECISION_TENTHS
    _state_feature: Incomplete
    _mode_feature: Incomplete
    _temp_feature: Incomplete
    _target_feature: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, parent: Device) -> None: ...
    @async_refresh_after
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @async_refresh_after
    async def async_turn_on(self) -> None: ...
    @async_refresh_after
    async def async_turn_off(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_action: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
    def _get_unique_id(self) -> str: ...
