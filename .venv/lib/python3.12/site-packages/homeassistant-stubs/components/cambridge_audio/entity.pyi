from .const import DOMAIN as DOMAIN, STREAM_MAGIC_EXCEPTIONS as STREAM_MAGIC_EXCEPTIONS
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient as StreamMagicClient
from aiostreammagic.models import CallbackType as CallbackType
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any, Concatenate

def command[_EntityT: CambridgeAudioEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Awaitable[None]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...

class CambridgeAudioEntity(Entity):
    _attr_has_entity_name: bool
    client: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, client: StreamMagicClient) -> None: ...
    _attr_available: Incomplete
    async def _state_update_callback(self, _client: StreamMagicClient, _callback_type: CallbackType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
