from .const import DOMAIN as DOMAIN
from .entity import PeblarEntity as PeblarEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def peblar_exception_handler[_PeblarEntityT: PeblarEntity, **_P](func: Callable[Concatenate[_PeblarEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_PeblarEntityT, _P], Coroutine[Any, Any, None]]: ...
