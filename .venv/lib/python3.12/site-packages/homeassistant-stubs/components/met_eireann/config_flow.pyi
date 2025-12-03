from .const import DOMAIN as DOMAIN, HOME_LOCATION_NAME as HOME_LOCATION_NAME
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from typing import Any

class MetEireannFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
