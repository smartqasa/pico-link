import voluptuous as vol
from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any, Concatenate

_LOGGER: Incomplete

class RequestDataValidator:
    _schema: Incomplete
    _allow_empty: Incomplete
    def __init__(self, schema: VolDictType | vol.Schema, allow_empty: bool = False) -> None: ...
    def __call__[_HassViewT: HomeAssistantView, **_P](self, method: Callable[Concatenate[_HassViewT, web.Request, dict[str, Any], _P], Awaitable[web.Response]]) -> Callable[Concatenate[_HassViewT, web.Request, _P], Coroutine[Any, Any, web.Response]]: ...
