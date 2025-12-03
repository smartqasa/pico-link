import voluptuous as vol
from .const import DOMAIN as DOMAIN
from .coordinator import Options as Options, OptionsValidationError as OptionsValidationError
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.config_entry_flow import DiscoveryFlowHandler as DiscoveryFlowHandler
from typing import Any

async def _async_has_devices(hass: HomeAssistant) -> bool: ...

class WemoFlow(DiscoveryFlowHandler, domain=DOMAIN):
    def __init__(self) -> None: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class WemoOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

def _schema_for_options(options: Options) -> vol.Schema: ...
