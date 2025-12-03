from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData, SleepIQPauseUpdateCoordinator as SleepIQPauseUpdateCoordinator
from .entity import SleepIQBedEntity as SleepIQBedEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepNumberPrivateSwitch(SleepIQBedEntity[SleepIQPauseUpdateCoordinator], SwitchEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SleepIQPauseUpdateCoordinator, bed: SleepIQBed) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
