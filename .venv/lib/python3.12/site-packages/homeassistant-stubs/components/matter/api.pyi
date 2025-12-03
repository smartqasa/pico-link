from .adapter import MatterAdapter as MatterAdapter
from .helpers import MissingNode as MissingNode, get_matter as get_matter, node_from_ha_device_id as node_from_ha_device_id
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from matter_server.client.models.node import MatterNode as MatterNode
from typing import Any, Concatenate

ID: str
TYPE: str
DEVICE_ID: str
ERROR_NODE_NOT_FOUND: str

@callback
def async_register_api(hass: HomeAssistant) -> None: ...
def async_get_node(func: Callable[[HomeAssistant, ActiveConnection, dict[str, Any], MatterAdapter, MatterNode], Coroutine[Any, Any, None]]) -> Callable[[HomeAssistant, ActiveConnection, dict[str, Any], MatterAdapter], Coroutine[Any, Any, None]]: ...
def async_get_matter_adapter(func: Callable[[HomeAssistant, ActiveConnection, dict[str, Any], MatterAdapter], Coroutine[Any, Any, None]]) -> Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Coroutine[Any, Any, None]]: ...
def async_handle_failed_command[**_P](func: Callable[Concatenate[HomeAssistant, ActiveConnection, dict[str, Any], _P], Coroutine[Any, Any, None]]) -> Callable[Concatenate[HomeAssistant, ActiveConnection, dict[str, Any], _P], Coroutine[Any, Any, None]]: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
async def websocket_commission(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
async def websocket_commission_on_network(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
async def websocket_set_thread_dataset(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
async def websocket_set_wifi_credentials(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter) -> None: ...
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
@async_get_node
async def websocket_node_diagnostics(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter, node: MatterNode) -> None: ...
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
@async_get_node
async def websocket_ping_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter, node: MatterNode) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
@async_get_node
async def websocket_open_commissioning_window(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter, node: MatterNode) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
@async_get_node
async def websocket_remove_matter_fabric(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter, node: MatterNode) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_matter_adapter
@async_get_node
async def websocket_interview_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], matter: MatterAdapter, node: MatterNode) -> None: ...
