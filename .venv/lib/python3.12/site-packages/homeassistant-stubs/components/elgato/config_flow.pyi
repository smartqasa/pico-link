from .const import DOMAIN as DOMAIN
from homeassistant.components import onboarding as onboarding, zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class ElgatoFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str
    port: int
    serial_number: str
    mac: str | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, _: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_show_setup_form(self, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_create_entry(self) -> ConfigFlowResult: ...
    async def _get_elgato_serial_number(self, raise_on_progress: bool = True) -> None: ...
