from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from ..models import AuthFlowContext as AuthFlowContext, AuthFlowResult as AuthFlowResult, Credentials as Credentials, UserMeta as UserMeta
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

USER_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

class InvalidAuthError(HomeAssistantError): ...

class ExampleAuthProvider(AuthProvider):
    async def async_login_flow(self, context: AuthFlowContext | None) -> ExampleLoginFlow: ...
    @callback
    def async_validate_login(self, username: str, password: str) -> None: ...
    async def async_get_or_create_credentials(self, flow_result: Mapping[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...

class ExampleLoginFlow(LoginFlow[ExampleAuthProvider]):
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> AuthFlowResult: ...
