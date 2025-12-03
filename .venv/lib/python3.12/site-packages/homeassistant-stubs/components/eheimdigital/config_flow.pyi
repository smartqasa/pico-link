from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers import selector as selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

CONFIG_SCHEMA: Incomplete

class EheimDigitalConfigFlow(ConfigFlow, domain=DOMAIN):
    data: dict[str, Any]
    main_device_added_event: Incomplete
    def __init__(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
