from .const import ATTR_ADAPTERS as ATTR_ADAPTERS, ATTR_CONFIGURED_ADAPTERS as ATTR_CONFIGURED_ADAPTERS, NETWORK_CONFIG_SCHEMA as NETWORK_CONFIG_SCHEMA
from .network import async_get_network as async_get_network
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from typing import Any

@callback
def async_register_websocket_commands(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_network_adapters(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_network_adapters_configure(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def websocket_network_url(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
