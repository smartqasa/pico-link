from .const import CONF_AZIMUTH as CONF_AZIMUTH, CONF_DAMPING_EVENING as CONF_DAMPING_EVENING, CONF_DAMPING_MORNING as CONF_DAMPING_MORNING, CONF_DECLINATION as CONF_DECLINATION, CONF_INVERTER_SIZE as CONF_INVERTER_SIZE, CONF_MODULES_POWER as CONF_MODULES_POWER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from typing import Any

RE_API_KEY: Incomplete

class ForecastSolarFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> ForecastSolarOptionFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class ForecastSolarOptionFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
