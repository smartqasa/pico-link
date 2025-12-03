from .config import ScheduleState as ScheduleState
from .const import DATA_MANAGER as DATA_MANAGER, LOGGER as LOGGER
from .manager import IncorrectPasswordError as IncorrectPasswordError, ManagerStateEvent as ManagerStateEvent
from .models import Folder as Folder
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_register_websocket_handlers(hass: HomeAssistant, with_hassio: bool) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_details(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_delete(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_restore(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_create(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_create_with_automatic_settings(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def handle_backup_start(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def handle_backup_end(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def backup_agents_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_config_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_config_update(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_subscribe_events(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
