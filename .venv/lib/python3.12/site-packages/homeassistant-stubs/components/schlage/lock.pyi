from . import SchlageConfigEntry as SchlageConfigEntry
from .coordinator import LockData as LockData, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from .entity import SchlageEntity as SchlageEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: SchlageConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SchlageLockEntity(SchlageEntity, LockEntity):
    _attr_name: Incomplete
    def __init__(self, coordinator: SchlageDataUpdateCoordinator, device_id: str) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_locked: Incomplete
    _attr_is_jammed: Incomplete
    _attr_changed_by: Incomplete
    def _update_attrs(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
