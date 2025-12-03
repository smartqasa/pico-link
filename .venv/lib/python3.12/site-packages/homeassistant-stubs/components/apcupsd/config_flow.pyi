from .const import CONNECTION_TIMEOUT as CONNECTION_TIMEOUT, DOMAIN as DOMAIN
from .coordinator import APCUPSdData as APCUPSdData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.helpers import selector as selector
from typing import Any

_PORT_SELECTOR: Incomplete
_SCHEMA: Incomplete

class ConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
