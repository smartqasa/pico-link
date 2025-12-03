from .const import DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PORT as DEFAULT_PORT, DEVICE_TIMEOUT_SECONDS as DEVICE_TIMEOUT_SECONDS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from anthemav.connection import Connection as Connection
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_PORT as CONF_PORT
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def connect_device(user_input: dict[str, Any]) -> Connection: ...

class AnthemAVConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
