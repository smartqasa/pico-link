from .const import DOMAIN as DOMAIN
from collections.abc import Iterator
from contextlib import contextmanager
from homeassistant.components.trace import ActionTrace as ActionTrace, CONF_STORED_TRACES as CONF_STORED_TRACES, async_store_trace as async_store_trace
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from typing import Any

class ScriptTrace(ActionTrace):
    _domain = DOMAIN

@contextmanager
def trace_script(hass: HomeAssistant, item_id: str, config: dict[str, Any] | None, blueprint_inputs: dict[str, Any] | None, context: Context, trace_config: dict[str, Any]) -> Iterator[ScriptTrace]: ...
