from .const import DOMAIN as DOMAIN
from aioairzone_cloud.cloudapi import AirzoneCloudApi
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ID as CONF_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

class AirZoneCloudConfigFlow(ConfigFlow, domain=DOMAIN):
    airzone: AirzoneCloudApi
    async def async_step_inst_pick(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
