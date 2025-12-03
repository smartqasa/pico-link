from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.util.executor import InterruptibleThreadPoolExecutor as InterruptibleThreadPoolExecutor
from typing import Any

def _worker_with_shutdown_hook(shutdown_hook: Callable[[], None], recorder_and_worker_thread_ids: set[int], *args: Any, **kwargs: Any) -> None: ...

class DBInterruptibleThreadPoolExecutor(InterruptibleThreadPoolExecutor):
    _shutdown_hook: Callable[[], None]
    recorder_and_worker_thread_ids: Incomplete
    def __init__(self, recorder_and_worker_thread_ids: set[int], *args: Any, **kwargs: Any) -> None: ...
    def _adjust_thread_count(self) -> None: ...
