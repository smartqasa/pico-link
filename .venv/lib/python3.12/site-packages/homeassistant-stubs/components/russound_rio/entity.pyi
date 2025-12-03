from .const import DOMAIN as DOMAIN, RUSSOUND_RIO_EXCEPTIONS as RUSSOUND_RIO_EXCEPTIONS
from _typeshed import Incomplete
from aiorussound import Controller as Controller, RussoundClient as RussoundClient
from aiorussound.models import CallbackType
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any, Concatenate

def command[_EntityT: RussoundBaseEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Awaitable[None]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...

class RussoundBaseEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _client: Incomplete
    _controller: Incomplete
    _primary_mac_address: Incomplete
    _device_identifier: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, controller: Controller) -> None: ...
    _attr_available: Incomplete
    async def _state_update_callback(self, _client: RussoundClient, _callback_type: CallbackType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
