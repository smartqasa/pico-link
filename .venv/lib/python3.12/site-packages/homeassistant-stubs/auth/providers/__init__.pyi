import types
from ..auth_store import AuthStore as AuthStore
from ..const import MFA_SESSION_EXPIRATION as MFA_SESSION_EXPIRATION
from ..models import AuthFlowContext as AuthFlowContext, AuthFlowResult as AuthFlowResult, Credentials as Credentials, RefreshToken as RefreshToken, User as User, UserMeta as UserMeta
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import requirements as requirements
from homeassistant.const import CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowHandler as FlowHandler
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.importlib import async_import_module as async_import_module
from homeassistant.util.decorator import Registry as Registry
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Generic
from typing_extensions import TypeVar

_LOGGER: Incomplete
DATA_REQS: HassKey[set[str]]
AUTH_PROVIDERS: Registry[str, type[AuthProvider]]
AUTH_PROVIDER_SCHEMA: Incomplete
_AuthProviderT = TypeVar('_AuthProviderT', bound='AuthProvider', default='AuthProvider')

class AuthProvider:
    DEFAULT_TITLE: str
    hass: Incomplete
    store: Incomplete
    config: Incomplete
    def __init__(self, hass: HomeAssistant, store: AuthStore, config: dict[str, Any]) -> None: ...
    @property
    def id(self) -> str | None: ...
    @property
    def type(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def support_mfa(self) -> bool: ...
    async def async_credentials(self) -> list[Credentials]: ...
    @callback
    def async_create_credentials(self, data: dict[str, str]) -> Credentials: ...
    async def async_login_flow(self, context: AuthFlowContext | None) -> LoginFlow[Any]: ...
    async def async_get_or_create_credentials(self, flow_result: Mapping[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...
    async def async_initialize(self) -> None: ...
    @callback
    def async_validate_refresh_token(self, refresh_token: RefreshToken, remote_ip: str | None = None) -> None: ...

async def auth_provider_from_config(hass: HomeAssistant, store: AuthStore, config: dict[str, Any]) -> AuthProvider: ...
async def load_auth_provider_module(hass: HomeAssistant, provider: str) -> types.ModuleType: ...

class LoginFlow(FlowHandler[AuthFlowContext, AuthFlowResult, tuple[str, str]], Generic[_AuthProviderT]):
    _flow_result = AuthFlowResult
    _auth_provider: Incomplete
    _auth_module_id: str | None
    _auth_manager: Incomplete
    available_mfa_modules: dict[str, str]
    created_at: Incomplete
    invalid_mfa_times: int
    user: User | None
    credential: Credentials | None
    def __init__(self, auth_provider: _AuthProviderT) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> AuthFlowResult: ...
    async def async_step_select_mfa_module(self, user_input: dict[str, str] | None = None) -> AuthFlowResult: ...
    async def async_step_mfa(self, user_input: dict[str, str] | None = None) -> AuthFlowResult: ...
    async def async_finish(self, flow_result: Any) -> AuthFlowResult: ...
