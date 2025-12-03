from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from ..models import AuthFlowContext as AuthFlowContext, AuthFlowResult as AuthFlowResult, Credentials as Credentials, UserMeta as UserMeta
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_COMMAND as CONF_COMMAND
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

CONF_ARGS: str
CONF_META: str
CONFIG_SCHEMA: Incomplete
_LOGGER: Incomplete

class InvalidAuthError(HomeAssistantError): ...

class CommandLineAuthProvider(AuthProvider):
    DEFAULT_TITLE: str
    ALLOWED_META_KEYS: Incomplete
    _user_meta: dict[str, dict[str, Any]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def async_login_flow(self, context: AuthFlowContext | None) -> CommandLineLoginFlow: ...
    async def async_validate_login(self, username: str, password: str) -> None: ...
    async def async_get_or_create_credentials(self, flow_result: Mapping[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...

class CommandLineLoginFlow(LoginFlow[CommandLineAuthProvider]):
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> AuthFlowResult: ...
