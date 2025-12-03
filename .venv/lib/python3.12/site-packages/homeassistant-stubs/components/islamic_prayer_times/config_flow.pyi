from .const import CALC_METHODS as CALC_METHODS, CONF_CALC_METHOD as CONF_CALC_METHOD, CONF_LAT_ADJ_METHOD as CONF_LAT_ADJ_METHOD, CONF_MIDNIGHT_MODE as CONF_MIDNIGHT_MODE, CONF_SCHOOL as CONF_SCHOOL, DEFAULT_CALC_METHOD as DEFAULT_CALC_METHOD, DEFAULT_LAT_ADJ_METHOD as DEFAULT_LAT_ADJ_METHOD, DEFAULT_MIDNIGHT_MODE as DEFAULT_MIDNIGHT_MODE, DEFAULT_SCHOOL as DEFAULT_SCHOOL, DOMAIN as DOMAIN, LAT_ADJ_METHODS as LAT_ADJ_METHODS, MIDNIGHT_MODES as MIDNIGHT_MODES, NAME as NAME, SCHOOLS as SCHOOLS
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import LocationSelector as LocationSelector, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector
from typing import Any

class IslamicPrayerFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> IslamicPrayerOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class IslamicPrayerOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
