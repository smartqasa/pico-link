from .const import DOMAIN as DOMAIN
from homeassistant.components import webhook as webhook
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import get_url as get_url
from typing import Any

class EcowittConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _webhook_id: str
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InvalidPort(HomeAssistantError): ...
