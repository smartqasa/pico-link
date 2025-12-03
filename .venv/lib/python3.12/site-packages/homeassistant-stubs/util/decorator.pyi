from collections.abc import Callable as Callable, Hashable as Hashable
from typing import Any

class Registry[_KT: Hashable, _VT: Callable[..., Any]](dict[_KT, _VT]):
    def register(self, name: _KT) -> Callable[[_VT], _VT]: ...
