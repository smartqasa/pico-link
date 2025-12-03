from .const import CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_LOCKED_UNLOCKED_KEY as CHARGER_LOCKED_UNLOCKED_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, DOMAIN as DOMAIN
from .coordinator import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator
from .entity import WallboxEntity as WallboxEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOCK_TYPES: dict[str, LockEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxLock(WallboxEntity, LockEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, description: LockEntityDescription) -> None: ...
    @property
    def is_locked(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
