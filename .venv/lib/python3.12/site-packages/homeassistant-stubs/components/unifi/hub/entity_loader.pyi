from ..const import LOGGER as LOGGER, UNIFI_WIRELESS_CLIENTS as UNIFI_WIRELESS_CLIENTS
from ..entity import UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription
from .hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Sequence
from homeassistant.const import Platform as Platform
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

CHECK_HEARTBEAT_INTERVAL: Incomplete
POLL_INTERVAL: Incomplete

class UnifiEntityLoader:
    hub: Incomplete
    api_updaters: Incomplete
    polling_api_updaters: Incomplete
    wireless_clients: Incomplete
    _dataUpdateCoordinator: Incomplete
    _update_listener: Incomplete
    platforms: list[tuple[AddEntitiesCallback, type[UnifiEntity], tuple[UnifiEntityDescription, ...], bool]]
    known_objects: set[tuple[str, str]]
    def __init__(self, hub: UnifiHub) -> None: ...
    async def initialize(self) -> None: ...
    async def _refresh_data(self, updaters: Sequence[Callable[[], Coroutine[Any, Any, None]]]) -> None: ...
    async def _update_pollable_api_data(self) -> None: ...
    async def _refresh_api_data(self) -> None: ...
    @callback
    def _restore_inactive_clients(self) -> None: ...
    @callback
    def register_platform(self, async_add_entities: AddEntitiesCallback, entity_class: type[UnifiEntity], descriptions: tuple[UnifiEntityDescription, ...], requires_admin: bool = False) -> None: ...
    @callback
    def load_entities(self) -> None: ...
    @callback
    def _should_add_entity(self, description: UnifiEntityDescription, obj_id: str) -> bool: ...
    @callback
    def _load_entities(self, unifi_platform_entity: type[UnifiEntity], descriptions: tuple[UnifiEntityDescription, ...], async_add_entities: AddEntitiesCallback) -> None: ...
