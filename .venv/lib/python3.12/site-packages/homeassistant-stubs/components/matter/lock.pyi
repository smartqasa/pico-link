import asyncio
from .const import LOGGER as LOGGER
from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription, LockEntityFeature as LockEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DoorLockFeature: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterLock(MatterEntity, LockEntity):
    _feature_map: int | None
    _optimistic_timer: asyncio.TimerHandle | None
    _platform_translation_key: str
    @property
    def code_format(self) -> str | None: ...
    async def send_device_command(self, command: clusters.ClusterCommand, timed_request_timeout_ms: int = 1000) -> None: ...
    _attr_is_locking: bool
    async def async_lock(self, **kwargs: Any) -> None: ...
    _attr_is_unlocking: bool
    async def async_unlock(self, **kwargs: Any) -> None: ...
    _attr_is_opening: bool
    async def async_open(self, **kwargs: Any) -> None: ...
    _attr_is_locked: bool
    _attr_is_open: bool
    @callback
    def _update_from_device(self) -> None: ...
    @callback
    def _reset_optimistic_state(self, write_state: bool = True) -> None: ...
    _attr_supported_features: Incomplete
    @callback
    def _calculate_features(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
