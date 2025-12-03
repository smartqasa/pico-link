from .const import DOMAIN as DOMAIN
from .coordinator import SurePetcareDataCoordinator as SurePetcareDataCoordinator
from .entity import SurePetcareEntity as SurePetcareEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockState as LockState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from surepy.entities import SurepyEntity as SurepyEntity
from surepy.enums import LockState as SurepyLockState
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SurePetcareLock(SurePetcareEntity, LockEntity):
    _lock_state: Incomplete
    _available: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator, lock_state: SurepyLockState) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_is_locked: Incomplete
    @callback
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...
    _attr_is_locking: bool
    async def async_lock(self, **kwargs: Any) -> None: ...
    _attr_is_unlocking: bool
    async def async_unlock(self, **kwargs: Any) -> None: ...
