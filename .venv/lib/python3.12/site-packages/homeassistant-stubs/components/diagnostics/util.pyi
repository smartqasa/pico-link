from .const import REDACTED as REDACTED
from collections.abc import Iterable, Mapping
from homeassistant.core import callback as callback
from typing import Any, overload

@overload
def async_redact_data(data: Mapping, to_redact: Iterable[Any]) -> dict: ...
@overload
def async_redact_data[_T](data: _T, to_redact: Iterable[Any]) -> _T: ...
