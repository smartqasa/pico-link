from . import importer as importer, models as models
from .const import DOMAIN as DOMAIN
from .errors import BlueprintException as BlueprintException, FailedToLoad as FailedToLoad, FileAlreadyExists as FileAlreadyExists
from .schemas import BLUEPRINT_SCHEMA as BLUEPRINT_SCHEMA
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util import yaml as yaml
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
def _ws_with_blueprint_domain(func: Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any], models.DomainBlueprints], Coroutine[Any, Any, None]]) -> websocket_api.AsyncWebSocketCommandHandler: ...
@websocket_api.async_response
async def ws_list_blueprints(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def ws_import_blueprint(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@_ws_with_blueprint_domain
async def ws_save_blueprint(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], domain_blueprints: models.DomainBlueprints) -> None: ...
@websocket_api.async_response
@_ws_with_blueprint_domain
async def ws_delete_blueprint(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], domain_blueprints: models.DomainBlueprints) -> None: ...
@websocket_api.async_response
@_ws_with_blueprint_domain
async def ws_substitute_blueprint(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], domain_blueprints: models.DomainBlueprints) -> None: ...
