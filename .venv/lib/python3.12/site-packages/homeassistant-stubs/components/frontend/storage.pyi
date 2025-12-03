from collections.abc import Callable as Callable, Coroutine
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import Any

DATA_STORAGE: str
STORAGE_VERSION_USER_DATA: int

@callback
def _initialize_frontend_storage(hass: HomeAssistant) -> None: ...
async def async_setup_frontend_storage(hass: HomeAssistant) -> None: ...
async def async_user_store(hass: HomeAssistant, user_id: str) -> tuple[Store, dict[str, Any]]: ...
def with_store(orig_func: Callable[[HomeAssistant, ActiveConnection, dict[str, Any], Store, dict[str, Any]], Coroutine[Any, Any, None]]) -> Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Coroutine[Any, Any, None]]: ...
@websocket_api.async_response
@with_store
async def websocket_set_user_data(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], store: Store, data: dict[str, Any]) -> None: ...
@websocket_api.async_response
@with_store
async def websocket_get_user_data(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], store: Store, data: dict[str, Any]) -> None: ...
