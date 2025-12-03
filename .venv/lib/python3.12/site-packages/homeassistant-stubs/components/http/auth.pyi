from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID, KEY_HASS_USER as KEY_HASS_USER
from _typeshed import Incomplete
from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from datetime import timedelta
from homeassistant.auth import jwt_wrapper as jwt_wrapper
from homeassistant.auth.const import GROUP_ID_READ_ONLY as GROUP_ID_READ_ONLY
from homeassistant.auth.models import User as User
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.http import current_request as current_request
from homeassistant.helpers.json import json_bytes as json_bytes
from homeassistant.helpers.network import is_cloud_connection as is_cloud_connection
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.network import is_local as is_local
from typing import Final

_LOGGER: Incomplete
DATA_API_PASSWORD: Final[str]
DATA_SIGN_SECRET: Final[str]
SIGN_QUERY_PARAM: Final[str]
SAFE_QUERY_PARAMS: Final[Incomplete]
STORAGE_VERSION: int
STORAGE_KEY: str
CONTENT_USER_NAME: str

@callback
def async_sign_path(hass: HomeAssistant, path: str, expiration: timedelta, *, refresh_token_id: str | None = None, use_content_user: bool = False) -> str: ...
@callback
def async_user_not_allowed_do_auth(hass: HomeAssistant, user: User, request: Request | None = None) -> str | None: ...
async def async_setup_auth(hass: HomeAssistant, app: Application) -> None: ...
