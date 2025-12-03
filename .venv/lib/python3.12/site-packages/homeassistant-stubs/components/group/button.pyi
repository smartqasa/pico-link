from .entity import GroupEntity as GroupEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, SERVICE_PRESS as SERVICE_PRESS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(_: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, __: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_button(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> ButtonGroup: ...

class ButtonGroup(GroupEntity, ButtonEntity):
    _attr_available: bool
    _attr_should_poll: bool
    _entity_ids: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str | None, name: str, entity_ids: list[str]) -> None: ...
    async def async_press(self) -> None: ...
    @callback
    def async_update_group_state(self) -> None: ...
