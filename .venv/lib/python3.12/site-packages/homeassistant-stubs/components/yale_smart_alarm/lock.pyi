from . import YaleConfigEntry as YaleConfigEntry
from .const import CONF_LOCK_CODE_DIGITS as CONF_LOCK_CODE_DIGITS, DEFAULT_LOCK_CODE_DIGITS as DEFAULT_LOCK_CODE_DIGITS, DOMAIN as DOMAIN, YALE_ALL_ERRORS as YALE_ALL_ERRORS
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleLockEntity as YaleLockEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockState as LockState
from homeassistant.const import ATTR_CODE as ATTR_CODE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from yalesmartalarmclient import YaleLock as YaleLock, YaleLockState

LOCK_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: YaleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleDoorlock(YaleLockEntity, LockEntity):
    _attr_name: Incomplete
    _attr_code_format: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, lock: YaleLock, code_format: int) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_set_lock(self, state: YaleLockState, code: str | None) -> None: ...
    @property
    def is_locked(self) -> bool | None: ...
    @property
    def is_open(self) -> bool | None: ...
