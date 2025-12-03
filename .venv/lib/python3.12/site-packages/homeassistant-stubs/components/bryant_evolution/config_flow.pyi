from .const import CONF_SYSTEM_ZONE as CONF_SYSTEM_ZONE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_FILENAME as CONF_FILENAME
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def _enumerate_sz(tty: str) -> list[tuple[int, int]]: ...

class BryantConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
