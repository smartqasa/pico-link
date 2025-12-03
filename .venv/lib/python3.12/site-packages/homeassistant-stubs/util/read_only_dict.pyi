from typing import Any

def _readonly(*args: Any, **kwargs: Any) -> Any: ...

class ReadOnlyDict[_KT, _VT](dict[_KT, _VT]):
    __setitem__ = _readonly
    __delitem__ = _readonly
    pop = _readonly
    popitem = _readonly
    clear = _readonly
    update = _readonly
    setdefault = _readonly
    def __copy__(self) -> dict[_KT, _VT]: ...
    def __deepcopy__(self, memo: Any) -> dict[_KT, _VT]: ...
