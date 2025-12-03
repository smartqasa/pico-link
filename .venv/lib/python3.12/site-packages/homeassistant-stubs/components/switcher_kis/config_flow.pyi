from .const import DOMAIN as DOMAIN
from .utils import async_discover_devices as async_discover_devices
from _typeshed import Incomplete
from aioswitcher.bridge import SwitcherBase as SwitcherBase
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from typing import Any, Final

_LOGGER: Incomplete
CONFIG_SCHEMA: Final[Incomplete]

class SwitcherFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    username: str | None
    token: str | None
    discovered_devices: dict[str, SwitcherBase]
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_credentials(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, user_input: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _create_entry(self) -> ConfigFlowResult: ...
