from .data import ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from uiprotect.data import Doorlock, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectLock(ProtectDeviceEntity, LockEntity):
    device: Doorlock
    entity_description: LockEntityDescription
    _state_attrs: Incomplete
    _attr_is_locked: bool
    _attr_is_locking: bool
    _attr_is_unlocking: bool
    _attr_is_jammed: bool
    _attr_available: bool
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
