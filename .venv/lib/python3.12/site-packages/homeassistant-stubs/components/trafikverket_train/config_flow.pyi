from .const import CONF_FILTER_PRODUCT as CONF_FILTER_PRODUCT, CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from .util import next_departuredate as next_departuredate
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector, TimeSelector as TimeSelector
from typing import Any

_LOGGER: Incomplete
OPTION_SCHEMA: Incomplete
DATA_SCHEMA: Incomplete
DATA_SCHEMA_REAUTH: Incomplete

async def validate_input(hass: HomeAssistant, api_key: str, train_from: str, train_to: str, train_time: str | None, weekdays: list[str], product_filter: str | None) -> dict[str, str]: ...

class TVTrainConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> TVTrainOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class TVTrainOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
