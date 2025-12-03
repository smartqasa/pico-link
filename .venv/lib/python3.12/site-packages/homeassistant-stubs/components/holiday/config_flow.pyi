import voluptuous as vol
from .const import CONF_CATEGORIES as CONF_CATEGORIES, CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import CountrySelector as CountrySelector, CountrySelectorConfig as CountrySelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

SUPPORTED_COUNTRIES: Incomplete

def get_optional_categories(country: str) -> list[str]: ...
def get_options_schema(country: str) -> vol.Schema: ...

class HolidayConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: dict[str, Any]
    def __init__(self) -> None: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> HolidayOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_options(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class HolidayOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
