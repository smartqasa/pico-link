from .const import CONFIG_VERSION as CONFIG_VERSION, CONF_SOURCE_ID as CONF_SOURCE_ID, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .util import generate_source_id as generate_source_id
from _typeshed import Incomplete
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_URL as CONF_URL
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from typing import Any

LOGGER: Incomplete

class DlnaDmsFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION = CONFIG_VERSION
    _discoveries: dict[str, ssdp.SsdpServiceInfo]
    _location: str | None
    _usn: str | None
    _name: str | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _create_entry(self) -> ConfigFlowResult: ...
    async def _async_parse_discovery(self, discovery_info: ssdp.SsdpServiceInfo, raise_on_progress: bool = True) -> None: ...
    async def _async_get_discoveries(self) -> list[ssdp.SsdpServiceInfo]: ...
