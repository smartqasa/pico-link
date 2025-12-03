from .helpers.frame import get_current_frame as get_current_frame
from .util.loop import protect_loop as protect_loop
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from typing import Any

_IN_TESTS: Incomplete
ALLOWED_FILE_PREFIXES: Incomplete

def _check_import_call_allowed(mapped_args: dict[str, Any]) -> bool: ...
def _check_file_allowed(mapped_args: dict[str, Any]) -> bool: ...
def _check_sleep_call_allowed(mapped_args: dict[str, Any]) -> bool: ...
def _check_load_verify_locations_call_allowed(mapped_args: dict[str, Any]) -> bool: ...

@dataclass(slots=True, frozen=True)
class BlockingCall:
    original_func: Callable
    object: object
    function: str
    check_allowed: Callable[[dict[str, Any]], bool] | None
    strict: bool
    strict_core: bool
    skip_for_tests: bool

_BLOCKING_CALLS: tuple[BlockingCall, ...]

@dataclass(slots=True)
class BlockedCalls:
    calls: set[BlockingCall]

_BLOCKED_CALLS: Incomplete

def enable() -> None: ...
