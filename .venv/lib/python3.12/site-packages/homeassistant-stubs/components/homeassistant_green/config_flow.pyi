from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.hassio import HassioAPIError as HassioAPIError, async_get_green_settings as async_get_green_settings, async_set_green_settings as async_set_green_settings
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from homeassistant.helpers.hassio import is_hassio as is_hassio
from typing import Any

_LOGGER: Incomplete
STEP_HW_SETTINGS_SCHEMA: Incomplete

class HomeAssistantGreenConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> HomeAssistantGreenOptionsFlow: ...
    async def async_step_system(self, data: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class HomeAssistantGreenOptionsFlow(OptionsFlow):
    _hw_settings: dict[str, bool] | None
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_hardware_settings(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
