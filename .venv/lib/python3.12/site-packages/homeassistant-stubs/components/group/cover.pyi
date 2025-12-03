from .entity import GroupEntity as GroupEntity
from .util import reduce_attribute as reduce_attribute
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_CURRENT_TILT_POSITION as ATTR_CURRENT_TILT_POSITION, ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature, CoverState as CoverState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER, SERVICE_STOP_COVER_TILT as SERVICE_STOP_COVER_TILT, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

KEY_OPEN_CLOSE: str
KEY_STOP: str
KEY_POSITION: str
DEFAULT_NAME: str
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_cover(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> CoverGroup: ...

class CoverGroup(GroupEntity, CoverEntity):
    _attr_available: bool
    _attr_is_closed: bool | None
    _attr_is_opening: bool | None
    _attr_is_closing: bool | None
    _attr_current_cover_position: int | None
    _entity_ids: Incomplete
    _covers: dict[str, set[str]]
    _tilts: dict[str, set[str]]
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str | None, name: str, entities: list[str]) -> None: ...
    @callback
    def async_update_supported_features(self, entity_id: str, new_state: State | None) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    _attr_current_cover_tilt_position: Incomplete
    _attr_supported_features: Incomplete
    @callback
    def async_update_group_state(self) -> None: ...
