from .connection_test import CONNECTION_TEST_URL_BASE as CONNECTION_TEST_URL_BASE
from .const import AssistSatelliteEntityFeature as AssistSatelliteEntityFeature, CONNECTION_TEST_DATA as CONNECTION_TEST_DATA, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from .entity import AssistSatelliteEntity as AssistSatelliteEntity
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from typing import Any

CONNECTION_TEST_TIMEOUT: int

@callback
def async_register_websocket_api(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_intercept_wake_word(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_get_configuration(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_set_wake_words(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_test_connection(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
