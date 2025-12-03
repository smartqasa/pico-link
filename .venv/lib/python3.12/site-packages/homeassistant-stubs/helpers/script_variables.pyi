from . import template as template
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

class ScriptVariables:
    variables: Incomplete
    _has_template: bool | None
    def __init__(self, variables: dict[str, Any]) -> None: ...
    @callback
    def async_render(self, hass: HomeAssistant, run_variables: Mapping[str, Any] | None, *, render_as_defaults: bool = True, limited: bool = False) -> dict[str, Any]: ...
    def as_dict(self) -> dict[str, Any]: ...
