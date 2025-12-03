from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE
from homeassistant.core import callback as callback
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete

class LektricoFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _host: str
    _name: str
    _serial_number: str
    _board_revision: str
    _device_type: str
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_show_setup_form(self, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_create_entry(self) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _get_lektrico_device_settings_and_treat_unique_id(self) -> None: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
