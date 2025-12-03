from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from duotecno.unit import BaseUnit as BaseUnit
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any, Concatenate

class DuotecnoEntity(Entity):
    _attr_should_poll: bool
    _unit: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, unit: BaseUnit) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _on_update(self) -> None: ...
    @property
    def available(self) -> bool: ...

def api_call[_T: DuotecnoEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...
