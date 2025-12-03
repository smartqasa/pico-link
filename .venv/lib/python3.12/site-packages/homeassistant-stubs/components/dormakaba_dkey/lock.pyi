from .const import DOMAIN as DOMAIN
from .entity import DormakabaDkeyEntity as DormakabaDkeyEntity
from .models import DormakabaDkeyData as DormakabaDkeyData
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from py_dormakaba_dkey import DKEYLock as DKEYLock
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DormakabaDkeyLock(DormakabaDkeyEntity, LockEntity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[None], lock: DKEYLock) -> None: ...
    _attr_is_locked: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
