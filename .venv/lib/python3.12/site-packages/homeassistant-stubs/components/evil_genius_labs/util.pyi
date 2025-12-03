from .entity import EvilGeniusEntity as EvilGeniusEntity
from collections.abc import Awaitable, Callable as Callable, Coroutine
from typing import Any, Concatenate

def update_when_done[_EvilGeniusEntityT: EvilGeniusEntity, **_P, _R](func: Callable[Concatenate[_EvilGeniusEntityT, _P], Awaitable[_R]]) -> Callable[Concatenate[_EvilGeniusEntityT, _P], Coroutine[Any, Any, _R]]: ...
