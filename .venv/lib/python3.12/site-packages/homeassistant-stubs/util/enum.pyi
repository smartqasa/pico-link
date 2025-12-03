from collections.abc import Callable as Callable
from enum import Enum as Enum
from typing import Any

def lru_cache[_T: Callable[..., Any]](func: _T) -> _T: ...
@lru_cache
def try_parse_enum[_EnumT: Enum](cls, value: Any) -> _EnumT | None: ...
