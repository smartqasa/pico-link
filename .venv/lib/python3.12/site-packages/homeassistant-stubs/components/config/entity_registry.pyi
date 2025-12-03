from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ERR_NOT_FOUND as ERR_NOT_FOUND, require_admin as require_admin
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.json import json_dumps as json_dumps
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@callback
def websocket_list_entities(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

_ENTITY_CATEGORIES_JSON: Incomplete

@callback
def websocket_list_entities_for_display(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_get_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_get_entities(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@require_admin
@callback
def websocket_update_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@require_admin
@callback
def websocket_remove_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
