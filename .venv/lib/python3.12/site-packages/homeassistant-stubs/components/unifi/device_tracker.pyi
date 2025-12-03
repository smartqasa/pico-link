import aiounifi
from . import UnifiConfigEntry as UnifiConfigEntry
from .entity import HandlerT as HandlerT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_device_available_fn as async_device_available_fn
from .hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent
from aiounifi.models.api import ApiItemT
from aiounifi.models.event import Event, EventKey
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.components.device_tracker import ScannerEntity as ScannerEntity, ScannerEntityDescription as ScannerEntityDescription
from homeassistant.core import Event as core_Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from propcache import cached_property
from typing import Any

LOGGER: Incomplete
CLIENT_TRACKER: str
DEVICE_TRACKER: str
CLIENT_CONNECTED_ATTRIBUTES: Incomplete
CLIENT_STATIC_ATTRIBUTES: Incomplete
CLIENT_CONNECTED_ALL_ATTRIBUTES: Incomplete
WIRED_CONNECTION: Incomplete
WIRED_DISCONNECTION: Incomplete
WIRELESS_CONNECTION: Incomplete
WIRELESS_DISCONNECTION: Incomplete

@callback
def async_client_allowed_fn(hub: UnifiHub, obj_id: str) -> bool: ...
@callback
def async_client_is_connected_fn(hub: UnifiHub, obj_id: str) -> bool: ...
@callback
def async_device_heartbeat_timedelta_fn(hub: UnifiHub, obj_id: str) -> timedelta: ...

@dataclass(frozen=True, kw_only=True)
class UnifiTrackerEntityDescription(UnifiEntityDescription[HandlerT, ApiItemT], ScannerEntityDescription):
    heartbeat_timedelta_fn: Callable[[UnifiHub, str], timedelta]
    ip_address_fn: Callable[[aiounifi.Controller, str], str | None]
    is_connected_fn: Callable[[UnifiHub, str], bool]
    hostname_fn: Callable[[aiounifi.Controller, str], str | None]

ENTITY_DESCRIPTIONS: tuple[UnifiTrackerEntityDescription, ...]

@callback
def async_update_unique_id(hass: HomeAssistant, config_entry: UnifiConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: UnifiConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiScannerEntity(UnifiEntity[HandlerT, ApiItemT], ScannerEntity):
    entity_description: UnifiTrackerEntityDescription
    _event_is_on: set[EventKey]
    _ignore_events: bool
    _is_connected: bool
    @callback
    def async_initiate_state(self) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def hostname(self) -> str | None: ...
    @property
    def ip_address(self) -> str | None: ...
    @cached_property
    def mac_address(self) -> str: ...
    @cached_property
    def unique_id(self) -> str: ...
    @callback
    def _make_disconnected(self, *_: core_Event) -> None: ...
    @callback
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
    @callback
    def async_event_callback(self, event: Event) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
