from .thread import async_raise as async_raise
from _typeshed import Incomplete
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from typing import Any

_LOGGER: Incomplete
MAX_LOG_ATTEMPTS: int
_JOIN_ATTEMPTS: int
EXECUTOR_SHUTDOWN_TIMEOUT: int

def _log_thread_running_at_shutdown(name: str, ident: int) -> None: ...
def join_or_interrupt_threads(threads: set[Thread], timeout: float, log: bool) -> set[Thread]: ...

class InterruptibleThreadPoolExecutor(ThreadPoolExecutor):
    def shutdown(self, *args: Any, join_threads_or_timeout: bool = True, **kwargs: Any) -> None: ...
    def join_threads_or_timeout(self) -> None: ...
