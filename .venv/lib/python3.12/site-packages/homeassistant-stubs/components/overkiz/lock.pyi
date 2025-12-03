from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .entity import OverkizEntity as OverkizEntity
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizLock(OverkizEntity, LockEntity):
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    @property
    def is_locked(self) -> bool | None: ...
