from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

class AnovaConfligFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
