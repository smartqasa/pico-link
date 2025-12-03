from .const import DOMAIN as DOMAIN, FEATUREMAP_ATTRIBUTE_ID as FEATUREMAP_ATTRIBUTE_ID, ID_TYPE_DEVICE_ID as ID_TYPE_DEVICE_ID
from .discovery import MatterEntityInfo as MatterEntityInfo
from .helpers import get_device_id as get_device_id
from _typeshed import Incomplete
from chip.clusters.Objects import ClusterAttributeDescriptor as ClusterAttributeDescriptor
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import UndefinedType as UndefinedType
from matter_server.client import MatterClient as MatterClient
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint
from matter_server.common.models import EventType
from propcache import cached_property
from typing import Any

LOGGER: Incomplete

@dataclass(frozen=True)
class MatterEntityDescription(EntityDescription):
    measurement_to_ha: Callable[[Any], Any] | None = ...
    ha_to_native_value: Callable[[Any], Any] | None = ...

class MatterEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _name_postfix: str | None
    _platform_translation_key: str | None
    matter_client: Incomplete
    _endpoint: Incomplete
    _entity_info: Incomplete
    entity_description: Incomplete
    _unsubscribes: list[Callable]
    _attributes_map: dict[type, str]
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_available: Incomplete
    _attr_translation_key: Incomplete
    _attr_name: Incomplete
    def __init__(self, matter_client: MatterClient, endpoint: MatterEndpoint, entity_info: MatterEntityInfo) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @cached_property
    def name(self) -> str | UndefinedType | None: ...
    @callback
    def _on_matter_event(self, event: EventType, data: Any = None) -> None: ...
    @callback
    def _on_featuremap_update(self, event: EventType, data: tuple[int, str, int] | None) -> None: ...
    @callback
    def _update_from_device(self) -> None: ...
    @callback
    def get_matter_attribute_value(self, attribute: type[ClusterAttributeDescriptor], null_as_none: bool = True) -> Any: ...
    @callback
    def get_matter_attribute_path(self, attribute: type[ClusterAttributeDescriptor]) -> str: ...
