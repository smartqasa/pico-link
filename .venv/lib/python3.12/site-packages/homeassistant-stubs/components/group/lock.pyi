from .entity import GroupEntity as GroupEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature, LockState as LockState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SERVICE_LOCK as SERVICE_LOCK, SERVICE_OPEN as SERVICE_OPEN, SERVICE_UNLOCK as SERVICE_UNLOCK, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_lock(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> LockGroup: ...

class LockGroup(GroupEntity, LockEntity):
    _attr_available: bool
    _attr_should_poll: bool
    _entity_ids: Incomplete
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str | None, name: str, entity_ids: list[str]) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
    _attr_is_jammed: Incomplete
    _attr_is_locking: Incomplete
    _attr_is_opening: Incomplete
    _attr_is_open: Incomplete
    _attr_is_unlocking: Incomplete
    _attr_is_locked: Incomplete
    @callback
    def async_update_group_state(self) -> None: ...
