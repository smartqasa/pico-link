from .const import CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, CONF_USER_UUID as CONF_USER_UUID, DOMAIN as DOMAIN, LOGGER as LOGGER
from .util import async_get_client_with_credentials as async_get_client_with_credentials
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

AUTH_SCHEMA: Incomplete
REAUTH_SCHEMA: Incomplete

@dataclass(frozen=True, kw_only=True)
class CredentialsValidationResult:
    user_uuid: str | None = ...
    refresh_token: str | None = ...
    errors: dict[str, Any] = field(default_factory=dict)

async def async_validate_credentials(hass: HomeAssistant, username: str, password: str) -> CredentialsValidationResult: ...

class NotionFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
