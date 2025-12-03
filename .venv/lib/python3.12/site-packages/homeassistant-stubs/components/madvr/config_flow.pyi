from .const import DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from .errors import CannotConnect as CannotConnect
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from madvr.madvr import Madvr
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
RETRY_INTERVAL: int

class MadVRConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _handle_config_step(self, user_input: dict[str, Any] | None = None, step_id: str = 'user') -> ConfigFlowResult: ...

async def test_connection(hass: HomeAssistant, host: str, port: int) -> str: ...
async def close_test_connection(madvr_client: Madvr) -> None: ...
