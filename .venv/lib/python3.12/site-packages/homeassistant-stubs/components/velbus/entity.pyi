from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any, Concatenate
from velbusaio.channels import Channel as VelbusChannel

class VelbusEntity(Entity):
    _attr_should_poll: bool
    _channel: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, channel: VelbusChannel) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _on_update(self) -> None: ...

def api_call[_T: VelbusEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...
