from .entity import GroupEntity as GroupEntity
from _typeshed import Incomplete
from homeassistant.components.event import ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, ATTR_EVENT_TYPES as ATTR_EVENT_TYPES, EventEntity as EventEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(_: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, __: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_event(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> EventGroup: ...

class EventGroup(GroupEntity, EventEntity):
    _attr_available: bool
    _attr_should_poll: bool
    _entity_ids: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _attr_event_types: Incomplete
    def __init__(self, unique_id: str | None, name: str, entity_ids: list[str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_update_group_state(self) -> None: ...
