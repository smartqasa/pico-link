from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.network import is_ip_address as is_ip_address
from typing import Any

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def validate_host(hass: HomeAssistant, host: str) -> None: ...

class ValloxConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InvalidHost(HomeAssistantError): ...
