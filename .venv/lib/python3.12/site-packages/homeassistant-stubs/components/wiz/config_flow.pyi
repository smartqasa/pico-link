from .const import DEFAULT_NAME as DEFAULT_NAME, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN, WIZ_CONNECT_EXCEPTIONS as WIZ_CONNECT_EXCEPTIONS
from .discovery import async_discover_devices as async_discover_devices
from .utils import _short_mac as _short_mac, name_from_bulb_type_and_mac as name_from_bulb_type_and_mac
from _typeshed import Incomplete
from homeassistant.components import dhcp as dhcp, onboarding as onboarding
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.util.network import is_ip_address as is_ip_address
from pywizlight.discovery import DiscoveredBulb
from typing import Any

_LOGGER: Incomplete
CONF_DEVICE: str

class WizConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_device: DiscoveredBulb
    _name: str
    _discovered_devices: dict[str, DiscoveredBulb]
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: dict[str, str]) -> ConfigFlowResult: ...
    async def _async_handle_discovery(self) -> ConfigFlowResult: ...
    async def _async_connect_discovered_or_abort(self) -> None: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pick_device(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
