from .entity import GroupEntity as GroupEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str
CONF_ALL: str
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_switch(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> SwitchGroup: ...

class SwitchGroup(GroupEntity, SwitchEntity):
    _attr_available: bool
    _attr_should_poll: bool
    _entity_ids: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    mode: Incomplete
    def __init__(self, unique_id: str | None, name: str, entity_ids: list[str], mode: bool | None) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def async_update_group_state(self) -> None: ...
