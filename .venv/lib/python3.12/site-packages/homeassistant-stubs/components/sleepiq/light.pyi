from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator
from .entity import SleepIQBedEntity as SleepIQBedEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQLight as SleepIQLight
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQLightEntity(SleepIQBedEntity[SleepIQDataUpdateCoordinator], LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    light: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, light: SleepIQLight) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
