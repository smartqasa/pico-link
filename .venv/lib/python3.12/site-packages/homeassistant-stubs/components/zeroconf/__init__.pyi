import re
from .models import HaAsyncZeroconf as HaAsyncZeroconf, HaZeroconf as HaZeroconf
from .usage import install_multiple_zeroconf_catcher as install_multiple_zeroconf_catcher
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from homeassistant.helpers import discovery_flow as discovery_flow, instance_id as instance_id
from homeassistant.helpers.discovery_flow import DiscoveryKey as DiscoveryKey
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import HomeKitDiscoveredIntegration as HomeKitDiscoveredIntegration, ZeroconfMatcher as ZeroconfMatcher, async_get_homekit as async_get_homekit, async_get_zeroconf as async_get_zeroconf, bind_hass as bind_hass
from homeassistant.setup import async_when_setup_or_start as async_when_setup_or_start
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Final
from zeroconf import ServiceStateChange
from zeroconf.asyncio import AsyncServiceBrowser, AsyncServiceInfo

_LOGGER: Incomplete
DOMAIN: str
ZEROCONF_TYPE: str
HOMEKIT_TYPES: Incomplete
_HOMEKIT_MODEL_SPLITS: Incomplete
CONF_DEFAULT_INTERFACE: str
CONF_IPV6: str
DEFAULT_DEFAULT_INTERFACE: bool
DEFAULT_IPV6: bool
HOMEKIT_PAIRED_STATUS_FLAG: str
HOMEKIT_MODEL_LOWER: str
HOMEKIT_MODEL_UPPER: str
MAX_PROPERTY_VALUE_LEN: int
MAX_NAME_LEN: int
ATTR_DOMAIN: Final[str]
ATTR_NAME: Final[str]
ATTR_PROPERTIES: Final[str]
ATTR_PROPERTIES_ID: Final[str]
CONFIG_SCHEMA: Incomplete

@dataclass(slots=True)
class ZeroconfServiceInfo(BaseServiceInfo):
    ip_address: IPv4Address | IPv6Address
    ip_addresses: list[IPv4Address | IPv6Address]
    port: int | None
    hostname: str
    type: str
    name: str
    properties: dict[str, Any]
    @property
    def host(self) -> str: ...
    @property
    def addresses(self) -> list[str]: ...

@bind_hass
async def async_get_instance(hass: HomeAssistant) -> HaZeroconf: ...
@bind_hass
async def async_get_async_instance(hass: HomeAssistant) -> HaAsyncZeroconf: ...
async def _async_get_instance(hass: HomeAssistant, **zcargs: Any) -> HaAsyncZeroconf: ...
@callback
def _async_zc_has_functional_dual_stack() -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _build_homekit_model_lookups(homekit_models: dict[str, HomeKitDiscoveredIntegration]) -> tuple[dict[str, HomeKitDiscoveredIntegration], dict[re.Pattern, HomeKitDiscoveredIntegration]]: ...
def _filter_disallowed_characters(name: str) -> str: ...
async def _async_register_hass_zc_service(hass: HomeAssistant, aio_zc: HaAsyncZeroconf, uuid: str) -> None: ...
def _match_against_props(matcher: dict[str, str], props: dict[str, str | None]) -> bool: ...
def is_homekit_paired(props: dict[str, Any]) -> bool: ...

class ZeroconfDiscovery:
    hass: Incomplete
    zeroconf: Incomplete
    zeroconf_types: Incomplete
    homekit_model_lookups: Incomplete
    homekit_model_matchers: Incomplete
    async_service_browser: AsyncServiceBrowser | None
    def __init__(self, hass: HomeAssistant, zeroconf: HaZeroconf, zeroconf_types: dict[str, list[ZeroconfMatcher]], homekit_model_lookups: dict[str, HomeKitDiscoveredIntegration], homekit_model_matchers: dict[re.Pattern, HomeKitDiscoveredIntegration]) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_stop(self) -> None: ...
    @callback
    def _handle_config_entry_removed(self, entry: config_entries.ConfigEntry) -> None: ...
    def _async_dismiss_discoveries(self, name: str) -> None: ...
    @callback
    def async_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str, state_change: ServiceStateChange) -> None: ...
    @callback
    def _async_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str) -> None: ...
    async def _async_lookup_and_process_service_update(self, zeroconf: HaZeroconf, async_service_info: AsyncServiceInfo, service_type: str, name: str) -> None: ...
    @callback
    def _async_process_service_update(self, async_service_info: AsyncServiceInfo, service_type: str, name: str) -> None: ...

def async_get_homekit_discovery(homekit_model_lookups: dict[str, HomeKitDiscoveredIntegration], homekit_model_matchers: dict[re.Pattern, HomeKitDiscoveredIntegration], props: dict[str, Any]) -> HomeKitDiscoveredIntegration | None: ...
def info_from_service(service: AsyncServiceInfo) -> ZeroconfServiceInfo | None: ...
def _suppress_invalid_properties(properties: dict) -> None: ...
def _truncate_location_name_to_valid(location_name: str) -> str: ...
def _compile_fnmatch(pattern: str) -> re.Pattern: ...
def _memorized_fnmatch(name: str, pattern: str) -> bool: ...
