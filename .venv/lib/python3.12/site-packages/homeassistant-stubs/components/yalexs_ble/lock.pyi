from . import YALEXSBLEConfigEntry as YALEXSBLEConfigEntry
from .entity import YALEXSBLEEntity as YALEXSBLEEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from yalexs_ble import ConnectionInfo as ConnectionInfo, LockInfo as LockInfo, LockState as LockState

async def async_setup_entry(hass: HomeAssistant, entry: YALEXSBLEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleXSBLELock(YALEXSBLEEntity, LockEntity):
    _attr_name: Incomplete
    _attr_is_locked: bool
    _attr_is_locking: bool
    _attr_is_unlocking: bool
    _attr_is_jammed: bool
    @callback
    def _async_update_state(self, new_state: LockState, lock_info: LockInfo, connection_info: ConnectionInfo) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
