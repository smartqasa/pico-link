from .const import DOMAIN as DOMAIN, ENTRY_TITLE as ENTRY_TITLE
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_API_TOKEN as CONF_API_TOKEN
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class SwitchBotCloudConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
