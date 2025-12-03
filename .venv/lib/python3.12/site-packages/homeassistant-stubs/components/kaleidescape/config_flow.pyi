from . import KaleidescapeDeviceInfo as KaleidescapeDeviceInfo, UnsupportedError as UnsupportedError, validate_host as validate_host
from .const import DEFAULT_HOST as DEFAULT_HOST, DOMAIN as DOMAIN
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from typing import Any

ERROR_CANNOT_CONNECT: str
ERROR_UNSUPPORTED: str

class KaleidescapeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_device: KaleidescapeDeviceInfo
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict | None = None) -> ConfigFlowResult: ...
