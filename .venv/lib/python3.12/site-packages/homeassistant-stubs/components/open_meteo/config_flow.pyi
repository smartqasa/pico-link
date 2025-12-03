from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ZONE as CONF_ZONE
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig
from typing import Any

class OpenMeteoFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
