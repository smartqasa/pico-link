from . import YaleConfigEntry as YaleConfigEntry
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleLockEntity as YaleLockEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from yalesmartalarmclient import YaleLock as YaleLock

async def async_setup_entry(hass: HomeAssistant, entry: YaleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleAutolockSwitch(YaleLockEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, lock: YaleLock) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
