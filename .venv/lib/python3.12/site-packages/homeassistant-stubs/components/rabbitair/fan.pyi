from .const import DOMAIN as DOMAIN
from .coordinator import RabbitAirDataUpdateCoordinator as RabbitAirDataUpdateCoordinator
from .entity import RabbitAirBaseEntity as RabbitAirBaseEntity
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item
from typing import Any

SPEED_LIST: Incomplete
PRESET_MODE_AUTO: str
PRESET_MODE_MANUAL: str
PRESET_MODE_POLLEN: str
PRESET_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RabbitAirFanEntity(RabbitAirBaseEntity, FanEntity):
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_speed_count: Incomplete
    def __init__(self, coordinator: RabbitAirDataUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_percentage: int
    _attr_preset_mode: Incomplete
    def _get_state_from_coordinator_data(self) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
