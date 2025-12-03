from .const import CONF_HOUSE_LETTER as CONF_HOUSE_LETTER, CONF_HOUSE_NUMBER as CONF_HOUSE_NUMBER, CONF_POST_CODE as CONF_POST_CODE, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class TwenteMilieuFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def _show_setup_form(self, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
