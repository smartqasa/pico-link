from .assist_pipeline import async_create_cloud_pipeline as async_create_cloud_pipeline
from .client import CloudClient as CloudClient
from .const import DATA_CLOUD as DATA_CLOUD, EVENT_CLOUD_EVENT as EVENT_CLOUD_EVENT, LOGIN_MFA_TIMEOUT as LOGIN_MFA_TIMEOUT, PREF_ALEXA_REPORT_STATE as PREF_ALEXA_REPORT_STATE, PREF_DISABLE_2FA as PREF_DISABLE_2FA, PREF_ENABLE_ALEXA as PREF_ENABLE_ALEXA, PREF_ENABLE_CLOUD_ICE_SERVERS as PREF_ENABLE_CLOUD_ICE_SERVERS, PREF_ENABLE_GOOGLE as PREF_ENABLE_GOOGLE, PREF_GOOGLE_REPORT_STATE as PREF_GOOGLE_REPORT_STATE, PREF_GOOGLE_SECURE_DEVICES_PIN as PREF_GOOGLE_SECURE_DEVICES_PIN, PREF_REMOTE_ALLOW_REMOTE_ENABLE as PREF_REMOTE_ALLOW_REMOTE_ENABLE, PREF_TTS_DEFAULT_VOICE as PREF_TTS_DEFAULT_VOICE, REQUEST_TIMEOUT as REQUEST_TIMEOUT
from .google_config import CLOUD_GOOGLE as CLOUD_GOOGLE
from .repairs import async_manage_legacy_subscription_issue as async_manage_legacy_subscription_issue
from .subscription import async_subscription_info as async_subscription_info
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Awaitable, Callable as Callable, Coroutine
from hass_nabucasa import Cloud as Cloud, auth
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.homeassistant import exposed_entities as exposed_entities
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.const import CLOUD_NEVER_EXPOSED_ENTITIES as CLOUD_NEVER_EXPOSED_ENTITIES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.util.location import async_detect_location_info as async_detect_location_info
from http import HTTPStatus
from typing import Any, Concatenate

_LOGGER: Incomplete
_CLOUD_ERRORS: dict[type[Exception], tuple[HTTPStatus, str]]

class MFAExpiredOrNotStarted(auth.CloudError): ...

@callback
def async_setup(hass: HomeAssistant) -> None: ...
def _handle_cloud_errors[_HassViewT: HomeAssistantView, **_P](handler: Callable[Concatenate[_HassViewT, web.Request, _P], Awaitable[web.Response]]) -> Callable[Concatenate[_HassViewT, web.Request, _P], Coroutine[Any, Any, web.Response]]: ...
def _ws_handle_cloud_errors(handler: Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any]], Coroutine[None, None, None]]) -> Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any]], Coroutine[None, None, None]]: ...
def _process_cloud_exception(exc: Exception, where: str) -> tuple[HTTPStatus, str]: ...

class GoogleActionsSyncView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    @_handle_cloud_errors
    async def post(self, request: web.Request) -> web.Response: ...

class CloudLoginView(HomeAssistantView):
    _mfa_tokens: dict[str, str]
    _mfa_tokens_set_time: float
    url: str
    name: str
    @require_admin
    @_handle_cloud_errors
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class CloudLogoutView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    @_handle_cloud_errors
    async def post(self, request: web.Request) -> web.Response: ...

class CloudRegisterView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    @_handle_cloud_errors
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class CloudResendConfirmView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    @_handle_cloud_errors
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class CloudForgotPasswordView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    @_handle_cloud_errors
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

@websocket_api.require_admin
@websocket_api.async_response
async def websocket_cloud_remove_data(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_cloud_status(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _require_cloud_login(handler: Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any]], None]) -> Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any]], None]: ...
@_require_cloud_login
@websocket_api.async_response
async def websocket_subscription(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def validate_language_voice(value: tuple[str, str]) -> tuple[str, str]: ...
@_require_cloud_login
@websocket_api.async_response
async def websocket_update_prefs(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def websocket_hook_create(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def websocket_hook_delete(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def _account_data(hass: HomeAssistant, cloud: Cloud[CloudClient]) -> dict[str, Any]: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def websocket_remote_connect(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def websocket_remote_disconnect(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def google_assistant_get(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def google_assistant_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def google_assistant_update(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def alexa_get(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
@_ws_handle_cloud_errors
async def alexa_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@_require_cloud_login
@websocket_api.async_response
async def alexa_sync(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def thingtalk_convert(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def tts_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
