from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from typing import Any

class HardkernelConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_system(self, data: dict[str, Any] | None = None) -> ConfigFlowResult: ...
