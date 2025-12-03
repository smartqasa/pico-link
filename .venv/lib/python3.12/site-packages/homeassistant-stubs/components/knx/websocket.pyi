from . import KNXModule as KNXModule
from .const import DOMAIN as DOMAIN, KNX_MODULE_KEY as KNX_MODULE_KEY
from .storage.config_store import ConfigStoreException as ConfigStoreException
from .storage.const import CONF_DATA as CONF_DATA
from .storage.entity_store_schema import CREATE_ENTITY_BASE_SCHEMA as CREATE_ENTITY_BASE_SCHEMA, UPDATE_ENTITY_BASE_SCHEMA as UPDATE_ENTITY_BASE_SCHEMA
from .storage.entity_store_validation import EntityStoreValidationException as EntityStoreValidationException, EntityStoreValidationSuccess as EntityStoreValidationSuccess, validate_entity_data as validate_entity_data
from .telegrams import SIGNAL_KNX_TELEGRAM as SIGNAL_KNX_TELEGRAM, TelegramDict as TelegramDict
from collections.abc import Awaitable, Callable
from homeassistant.components import panel_custom as panel_custom, websocket_api as websocket_api
from homeassistant.components.http import StaticPathConfig as StaticPathConfig
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from homeassistant.util.ulid import ulid_now as ulid_now
from typing import Any, Final, overload
from xknx.telegram import Telegram as Telegram

URL_BASE: Final[str]

async def register_panel(hass: HomeAssistant) -> None: ...
type KnxWebSocketCommandHandler = Callable[[HomeAssistant, KNXModule, websocket_api.ActiveConnection, dict[str, Any]], None]
type KnxAsyncWebSocketCommandHandler = Callable[[HomeAssistant, KNXModule, websocket_api.ActiveConnection, dict[str, Any]], Awaitable[None]]
@overload
def provide_knx(func: KnxAsyncWebSocketCommandHandler) -> websocket_api.const.AsyncWebSocketCommandHandler: ...
@overload
def provide_knx(func: KnxWebSocketCommandHandler) -> websocket_api.const.WebSocketCommandHandler: ...
@websocket_api.require_admin
@provide_knx
@callback
def ws_info(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@provide_knx
async def ws_get_knx_project(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@provide_knx
async def ws_project_file_process(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@provide_knx
async def ws_project_file_remove(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@provide_knx
@callback
def ws_group_monitor_info(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@provide_knx
@callback
def ws_group_telegrams(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@callback
def ws_subscribe_telegram(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@callback
def ws_validate_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@provide_knx
async def ws_create_entity(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@provide_knx
async def ws_update_entity(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@provide_knx
async def ws_delete_entity(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@provide_knx
@callback
def ws_get_entity_entries(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@provide_knx
@callback
def ws_get_entity_config(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
@websocket_api.require_admin
@provide_knx
@callback
def ws_create_device(hass: HomeAssistant, knx: KNXModule, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
