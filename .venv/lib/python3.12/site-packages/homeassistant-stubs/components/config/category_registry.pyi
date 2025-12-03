from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import category_registry as cr
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@callback
def websocket_list_categories(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@callback
def websocket_create_category(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@callback
def websocket_delete_category(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@callback
def websocket_update_category(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def _entry_dict(entry: cr.CategoryEntry) -> dict[str, Any]: ...
