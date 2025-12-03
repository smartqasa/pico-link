import threading
from _typeshed import Incomplete
from typing import Any

THREADING_SHUTDOWN_TIMEOUT: int
_LOGGER: Incomplete

def deadlock_safe_shutdown() -> None: ...
def async_raise(tid: int, exctype: Any) -> None: ...

class ThreadWithException(threading.Thread):
    def raise_exc(self, exctype: Any) -> None: ...
