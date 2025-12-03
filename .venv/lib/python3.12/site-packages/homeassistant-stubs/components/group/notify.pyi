from .entity import GroupEntity as GroupEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TITLE as ATTR_TITLE, BaseNotificationService as BaseNotificationService, NotifyEntity as NotifyEntity, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ACTION as CONF_ACTION, CONF_ENTITIES as CONF_ENTITIES, CONF_SERVICE as CONF_SERVICE, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_SERVICES: str

def _backward_compat_schema(value: Any | None) -> Any: ...

PLATFORM_SCHEMA: Incomplete

def add_defaults(input_data: dict[str, Any], default_data: Mapping[str, Any]) -> dict[str, Any]: ...
async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> GroupNotifyPlatform: ...

class GroupNotifyPlatform(BaseNotificationService):
    hass: Incomplete
    entities: Incomplete
    def __init__(self, hass: HomeAssistant, entities: list[dict[str, Any]]) -> None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_notify(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> NotifyGroup: ...

class NotifyGroup(GroupEntity, NotifyEntity):
    _attr_available: bool
    _entity_ids: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str | None, name: str, entity_ids: list[str]) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
    @callback
    def async_update_group_state(self) -> None: ...
