from _typeshed import Incomplete
from homeassistant.auth.models import User as User
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

WS_TYPE_LIST: str
SCHEMA_WS_LIST: Incomplete
WS_TYPE_DELETE: str
SCHEMA_WS_DELETE: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_delete(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_create(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_update(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _user_info(user: User) -> dict[str, Any]: ...
