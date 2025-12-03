from . import TractiveClient as TractiveClient
from .const import DOMAIN as DOMAIN, SERVER_UNAVAILABLE as SERVER_UNAVAILABLE
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from typing import Any

class TractiveEntity(Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _user_id: Incomplete
    _tracker_id: Incomplete
    _client: Incomplete
    _dispatcher_signal: Incomplete
    def __init__(self, client: TractiveClient, trackable: dict[str, Any], tracker_details: dict[str, Any], dispatcher_signal: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: Incomplete
    @callback
    def handle_status_update(self, event: dict[str, Any]) -> None: ...
    @callback
    def handle_server_unavailable(self) -> None: ...
