from .const import CONF_HOSTNAME as CONF_HOSTNAME, CONF_IPV4 as CONF_IPV4, CONF_IPV6 as CONF_IPV6, CONF_IPV6_V4 as CONF_IPV6_V4, CONF_PORT_IPV6 as CONF_PORT_IPV6, CONF_RESOLVER as CONF_RESOLVER, CONF_RESOLVER_IPV6 as CONF_RESOLVER_IPV6, DEFAULT_HOSTNAME as DEFAULT_HOSTNAME, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_RESOLVER as DEFAULT_RESOLVER, DEFAULT_RESOLVER_IPV6 as DEFAULT_RESOLVER_IPV6, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from typing import Any

DATA_SCHEMA: Incomplete
DATA_SCHEMA_ADV: Incomplete

async def async_validate_hostname(hostname: str, resolver_ipv4: str, resolver_ipv6: str, port: int, port_ipv6: int) -> dict[str, bool]: ...

class DnsIPConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> DnsIPOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class DnsIPOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
