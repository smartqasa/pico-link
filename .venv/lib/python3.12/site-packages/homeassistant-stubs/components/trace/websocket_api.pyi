from .util import async_get_trace as async_get_trace, async_list_contexts as async_list_contexts, async_list_traces as async_list_traces
from _typeshed import Incomplete
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import DATA_DISPATCHER as DATA_DISPATCHER, async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.json import ExtendedJSONEncoder as ExtendedJSONEncoder
from homeassistant.helpers.script import SCRIPT_BREAKPOINT_HIT as SCRIPT_BREAKPOINT_HIT, SCRIPT_DEBUG_CONTINUE_ALL as SCRIPT_DEBUG_CONTINUE_ALL, breakpoint_clear as breakpoint_clear, breakpoint_clear_all as breakpoint_clear_all, breakpoint_list as breakpoint_list, breakpoint_set as breakpoint_set, debug_continue as debug_continue, debug_step as debug_step, debug_stop as debug_stop
from typing import Any

TRACE_DOMAINS: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_trace_get(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_trace_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_trace_contexts(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_breakpoint_set(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_breakpoint_clear(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_breakpoint_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_subscribe_breakpoint_events(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_debug_continue(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_debug_step(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_debug_stop(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
