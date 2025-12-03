from .const import DOMAIN as DOMAIN
from .utils import hash_from_url as hash_from_url
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Incomplete
DATA_SCHEMA: Incomplete

async def _validate_input(data: dict[str, Any]) -> dict[str, str]: ...

class NightscoutConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InputValidationError(HomeAssistantError):
    base: Incomplete
    def __init__(self, base: str) -> None: ...
