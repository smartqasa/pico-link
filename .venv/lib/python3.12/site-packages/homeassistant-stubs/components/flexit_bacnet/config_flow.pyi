from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_IP_ADDRESS as CONF_IP_ADDRESS
from typing import Any

_LOGGER: Incomplete
DEFAULT_DEVICE_ID: int
STEP_USER_DATA_SCHEMA: Incomplete

class FlexitBacnetConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
