from . import OTBRConfigEntry as OTBRConfigEntry
from .const import DEFAULT_CHANNEL as DEFAULT_CHANNEL, DOMAIN as DOMAIN
from .util import OTBRData as OTBRData, compose_default_network_name as compose_default_network_name, generate_random_pan_id as generate_random_pan_id, get_allowed_channel as get_allowed_channel, update_issues as update_issues
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import is_multiprotocol_url as is_multiprotocol_url
from homeassistant.components.thread import async_add_dataset as async_add_dataset, async_get_dataset as async_get_dataset
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
def async_get_otbr_data(orig_func: Callable[[HomeAssistant, websocket_api.ActiveConnection, dict, OTBRData], Coroutine[Any, Any, None]]) -> Callable[[HomeAssistant, websocket_api.ActiveConnection, dict], Coroutine[Any, Any, None]]: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_otbr_data
async def websocket_create_network(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, data: OTBRData) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_otbr_data
async def websocket_set_network(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, data: OTBRData) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_otbr_data
async def websocket_set_channel(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, data: OTBRData) -> None: ...
