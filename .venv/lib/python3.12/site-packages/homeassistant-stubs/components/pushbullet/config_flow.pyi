from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME
from homeassistant.helpers import selector as selector
from typing import Any

CONFIG_SCHEMA: Incomplete

class PushBulletConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
