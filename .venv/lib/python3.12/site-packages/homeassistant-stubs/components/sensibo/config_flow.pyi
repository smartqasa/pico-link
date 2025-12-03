from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .util import NoDevicesError as NoDevicesError, NoUsernameError as NoUsernameError, async_validate_api as async_validate_api
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.selector import TextSelector as TextSelector
from typing import Any

DATA_SCHEMA: Incomplete

async def validate_api(hass: HomeAssistant, api_key: str) -> tuple[str | None, dict[str, str]]: ...

class SensiboConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
