from .const import CONF_ARP_PING as CONF_ARP_PING, CONF_DETECTION_TIME as CONF_DETECTION_TIME, CONF_FORCE_DHCP as CONF_FORCE_DHCP, DEFAULT_API_PORT as DEFAULT_API_PORT, DEFAULT_DETECTION_TIME as DEFAULT_DETECTION_TIME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import get_api as get_api
from .errors import CannotConnect as CannotConnect, LoginError as LoginError
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import callback as callback
from typing import Any

class MikrotikFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> MikrotikOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...

class MikrotikOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_device_tracker(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
