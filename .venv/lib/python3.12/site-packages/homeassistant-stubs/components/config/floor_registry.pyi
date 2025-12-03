from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.floor_registry import FloorEntry as FloorEntry
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@callback
def websocket_list_floors(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@callback
def websocket_create_floor(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@callback
def websocket_delete_floor(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@callback
def websocket_update_floor(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def _entry_dict(entry: FloorEntry) -> dict[str, Any]: ...
