from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD
from typing import Any

STEP_REAUTH_SCHEMA: Incomplete
STEP_USER_SCHEMA: Incomplete

@dataclass
class ValidationResult:
    serial_number: str | None = ...
    errors: dict[str, Any] = field(default_factory=dict)

async def async_validate_credentials(ip_address: str, password: str) -> ValidationResult: ...

class AirVisualProFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry_data: Mapping[str, Any]
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
