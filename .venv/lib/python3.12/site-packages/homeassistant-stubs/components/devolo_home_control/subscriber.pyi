from _typeshed import Incomplete
from collections.abc import Callable as Callable

_LOGGER: Incomplete

class Subscriber:
    name: Incomplete
    callback: Incomplete
    def __init__(self, name: str, callback: Callable) -> None: ...
    def update(self, message: str) -> None: ...
