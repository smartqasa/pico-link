from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete

class GPSDConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def test_connection(host: str, port: int) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
