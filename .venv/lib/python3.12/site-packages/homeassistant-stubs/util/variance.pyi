from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from typing import overload

@overload
def ignore_variance[**_P](func: Callable[_P, int], ignored_variance: int) -> Callable[_P, int]: ...
@overload
def ignore_variance[**_P](func: Callable[_P, float], ignored_variance: float) -> Callable[_P, float]: ...
@overload
def ignore_variance[**_P](func: Callable[_P, datetime], ignored_variance: timedelta) -> Callable[_P, datetime]: ...
