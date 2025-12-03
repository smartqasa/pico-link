import voluptuous as vol
from .const import CONF_CANDLE_LIGHT_MINUTES as CONF_CANDLE_LIGHT_MINUTES, CONF_DIASPORA as CONF_DIASPORA, CONF_HAVDALAH_OFFSET_MINUTES as CONF_HAVDALAH_OFFSET_MINUTES, DEFAULT_CANDLE_LIGHT as DEFAULT_CANDLE_LIGHT, DEFAULT_DIASPORA as DEFAULT_DIASPORA, DEFAULT_HAVDALAH_OFFSET_MINUTES as DEFAULT_HAVDALAH_OFFSET_MINUTES, DEFAULT_LANGUAGE as DEFAULT_LANGUAGE, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LANGUAGE as CONF_LANGUAGE, CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_TIME_ZONE as CONF_TIME_ZONE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, LocationSelector as LocationSelector, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any

LANGUAGE: Incomplete
OPTIONS_SCHEMA: Incomplete
_LOGGER: Incomplete

def _get_data_schema(hass: HomeAssistant) -> vol.Schema: ...

class JewishCalendarConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> JewishCalendarOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class JewishCalendarOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
