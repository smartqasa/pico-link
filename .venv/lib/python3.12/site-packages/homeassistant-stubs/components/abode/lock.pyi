from . import AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from .entity import AbodeDevice as AbodeDevice
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jaraco.abode.devices.lock import Lock as Lock
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeLock(AbodeDevice, LockEntity):
    _device: Lock
    _attr_name: Incomplete
    def lock(self, **kwargs: Any) -> None: ...
    def unlock(self, **kwargs: Any) -> None: ...
    @property
    def is_locked(self) -> bool: ...
