from .view import HomeAssistantView as HomeAssistantView
from aiohttp.web import Request, Response, StreamResponse
from collections.abc import Callable, Coroutine
from homeassistant.auth.models import User as User
from homeassistant.exceptions import Unauthorized as Unauthorized
from typing import Any, Concatenate, overload

type _ResponseType = Response | StreamResponse
type _FuncType[_T, **_P, _R] = Callable[Concatenate[_T, Request, _P], Coroutine[Any, Any, _R]]
@overload
def require_admin[_HomeAssistantViewT: HomeAssistantView, **_P, _ResponseT: _ResponseType](_func: None = None, *, error: Unauthorized | None = None) -> Callable[[_FuncType[_HomeAssistantViewT, _P, _ResponseT]], _FuncType[_HomeAssistantViewT, _P, _ResponseT]]: ...
@overload
def require_admin[_HomeAssistantViewT: HomeAssistantView, **_P, _ResponseT: _ResponseType](_func: _FuncType[_HomeAssistantViewT, _P, _ResponseT]) -> _FuncType[_HomeAssistantViewT, _P, _ResponseT]: ...
