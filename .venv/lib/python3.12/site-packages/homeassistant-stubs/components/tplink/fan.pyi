from . import TPLinkConfigEntry as TPLinkConfigEntry
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from homeassistant.util.scaling import int_states_in_range as int_states_in_range
from kasa import Device as Device
from kasa.interfaces import Fan as FanInterface
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

SPEED_RANGE: Incomplete

class TPLinkFanEntity(CoordinatedTPLinkEntity, FanEntity):
    _attr_speed_count: Incomplete
    _attr_supported_features: Incomplete
    fan_module: Incomplete
    _attr_name: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, fan_module: FanInterface, parent: Device | None = None) -> None: ...
    @async_refresh_after
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    _attr_is_on: Incomplete
    _attr_percentage: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
