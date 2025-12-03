from .const import DOMAIN as DOMAIN
from .entity import PlugwiseEntity as PlugwiseEntity
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def plugwise_command[_PlugwiseEntityT: PlugwiseEntity, **_P, _R](func: Callable[Concatenate[_PlugwiseEntityT, _P], Awaitable[_R]]) -> Callable[Concatenate[_PlugwiseEntityT, _P], Coroutine[Any, Any, _R]]: ...
