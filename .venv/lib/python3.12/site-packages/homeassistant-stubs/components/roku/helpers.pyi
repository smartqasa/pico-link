from .entity import RokuEntity as RokuEntity
from collections.abc import Awaitable, Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

type _FuncType[_T, **_P] = Callable[Concatenate[_T, _P], Awaitable[Any]]
type _ReturnFuncType[_T, **_P] = Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]
def format_channel_name(channel_number: str, channel_name: str | None = None) -> str: ...
def roku_exception_handler[_RokuEntityT: RokuEntity, **_P](ignore_timeout: bool = False) -> Callable[[_FuncType[_RokuEntityT, _P]], _ReturnFuncType[_RokuEntityT, _P]]: ...
