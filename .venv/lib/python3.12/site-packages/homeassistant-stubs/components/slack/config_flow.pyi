from .const import CONF_DEFAULT_CHANNEL as CONF_DEFAULT_CHANNEL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers import aiohttp_client as aiohttp_client

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

class SlackFlowHandler(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def _async_try_connect(self, token: str) -> tuple[str, None] | tuple[None, dict[str, str]]: ...
