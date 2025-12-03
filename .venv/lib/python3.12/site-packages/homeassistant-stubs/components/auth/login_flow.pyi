from . import StoreResultType as StoreResultType, indieauth as indieauth
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Callable as Callable
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.auth import AuthManagerFlowManager as AuthManagerFlowManager, InvalidAuthError as InvalidAuthError
from homeassistant.auth.models import AuthFlowContext as AuthFlowContext, AuthFlowResult as AuthFlowResult, Credentials as Credentials
from homeassistant.auth.providers.trusted_networks import TrustedNetworksAuthProvider as TrustedNetworksAuthProvider
from homeassistant.components import onboarding as onboarding
from homeassistant.components.http import KEY_HASS as KEY_HASS
from homeassistant.components.http.auth import async_user_not_allowed_do_auth as async_user_not_allowed_do_auth
from homeassistant.components.http.ban import log_invalid_auth as log_invalid_auth, process_success_login as process_success_login, process_wrong_login as process_wrong_login
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.network import is_cloud_connection as is_cloud_connection
from homeassistant.util.network import is_local as is_local
from typing import Any

@callback
def async_setup(hass: HomeAssistant, store_result: Callable[[str, Credentials], str]) -> None: ...

class WellKnownOAuthInfoView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    async def get(self, request: web.Request) -> web.Response: ...

class AuthProvidersView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    async def get(self, request: web.Request) -> web.Response: ...

def _prepare_result_json(result: AuthFlowResult) -> AuthFlowResult: ...

class LoginFlowBaseView(HomeAssistantView):
    requires_auth: bool
    _flow_mgr: Incomplete
    _store_result: Incomplete
    def __init__(self, flow_mgr: AuthManagerFlowManager, store_result: StoreResultType) -> None: ...
    async def _async_flow_result_to_response(self, request: web.Request, client_id: str, result: AuthFlowResult) -> web.Response: ...

class LoginFlowIndexView(LoginFlowBaseView):
    url: str
    name: str
    async def get(self, request: web.Request) -> web.Response: ...
    @log_invalid_auth
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class LoginFlowResourceView(LoginFlowBaseView):
    url: str
    name: str
    async def get(self, request: web.Request) -> web.Response: ...
    @log_invalid_auth
    async def post(self, request: web.Request, data: dict[str, Any], flow_id: str) -> web.Response: ...
    async def delete(self, request: web.Request, flow_id: str) -> web.Response: ...
