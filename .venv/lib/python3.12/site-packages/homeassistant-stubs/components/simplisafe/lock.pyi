from . import SimpliSafe as SimpliSafe
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import SimpliSafeEntity as SimpliSafeEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.device.lock import Lock as Lock
from simplipy.system.v3 import SystemV3 as SystemV3
from simplipy.websocket import WebsocketEvent as WebsocketEvent
from typing import Any

ATTR_LOCK_LOW_BATTERY: str
ATTR_PIN_PAD_LOW_BATTERY: str
STATE_MAP_FROM_WEBSOCKET_EVENT: Incomplete
WEBSOCKET_EVENTS_TO_LISTEN_FOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimpliSafeLock(SimpliSafeEntity, LockEntity):
    _attr_name: Incomplete
    _device: Lock
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, lock: Lock) -> None: ...
    _attr_is_locked: bool
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    _attr_is_jammed: Incomplete
    @callback
    def async_update_from_rest_api(self) -> None: ...
    @callback
    def async_update_from_websocket_event(self, event: WebsocketEvent) -> None: ...
