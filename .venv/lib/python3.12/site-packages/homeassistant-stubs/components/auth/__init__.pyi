from . import indieauth as indieauth, login_flow as login_flow, mfa_setup_flow as mfa_setup_flow
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Callable
from homeassistant.auth import InvalidAuthError as InvalidAuthError
from homeassistant.auth.models import Credentials as Credentials, RefreshToken as RefreshToken, TOKEN_TYPE_LONG_LIVED_ACCESS_TOKEN as TOKEN_TYPE_LONG_LIVED_ACCESS_TOKEN, User as User
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import KEY_HASS as KEY_HASS
from homeassistant.components.http.auth import async_sign_path as async_sign_path, async_user_not_allowed_do_auth as async_user_not_allowed_do_auth
from homeassistant.components.http.ban import log_invalid_auth as log_invalid_auth
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2AuthorizeCallbackView as OAuth2AuthorizeCallbackView
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from multidict import MultiDictProxy
from typing import Any

DOMAIN: str
type StoreResultType = Callable[[str, Credentials], str]
type RetrieveResultType = Callable[[str, str], Credentials | None]
DATA_STORE: HassKey[StoreResultType]
CONFIG_SCHEMA: Incomplete
DELETE_CURRENT_TOKEN_DELAY: int

@bind_hass
def create_auth_code(hass: HomeAssistant, client_id: str, credential: Credentials) -> str: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class RevokeTokenView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    cors_allowed: bool
    async def post(self, request: web.Request) -> web.Response: ...

class TokenView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    cors_allowed: bool
    _retrieve_auth: Incomplete
    def __init__(self, retrieve_auth: RetrieveResultType) -> None: ...
    @log_invalid_auth
    async def post(self, request: web.Request) -> web.Response: ...
    async def _async_handle_auth_code(self, hass: HomeAssistant, data: MultiDictProxy[str], request: web.Request) -> web.Response: ...
    async def _async_handle_refresh_token(self, hass: HomeAssistant, data: MultiDictProxy[str], request: web.Request) -> web.Response: ...

class LinkUserView(HomeAssistantView):
    url: str
    name: str
    _retrieve_credentials: Incomplete
    def __init__(self, retrieve_credentials: RetrieveResultType) -> None: ...
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

@callback
def _create_auth_code_store() -> tuple[StoreResultType, RetrieveResultType]: ...
@websocket_api.async_response
async def websocket_current_user(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_create_long_lived_access_token(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_refresh_tokens(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_delete_refresh_token(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_delete_all_refresh_tokens(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_sign_path(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_refresh_token_set_expiry(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
