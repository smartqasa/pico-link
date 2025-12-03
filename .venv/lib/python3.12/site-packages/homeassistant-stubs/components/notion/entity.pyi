from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import NotionDataUpdateCoordinator as NotionDataUpdateCoordinator
from _typeshed import Incomplete
from aionotion.bridge.models import Bridge as Bridge
from aionotion.listener.models import Listener as Listener, ListenerKind as ListenerKind
from dataclasses import dataclass
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class NotionEntityDescription:
    listener_kind: ListenerKind

class NotionEntity(CoordinatorEntity[NotionDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _bridge_id: Incomplete
    _listener_id: Incomplete
    _sensor_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: NotionDataUpdateCoordinator, listener_id: str, sensor_id: str, bridge_id: int, description: EntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def listener(self) -> Listener: ...
    @callback
    def _async_get_bridge(self, bridge_id: int) -> Bridge | None: ...
    @callback
    def _async_update_bridge_id(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
