import aiodhcpwatcher
import asyncio
import re
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiodiscover import DiscoverHosts
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.components.device_tracker import ATTR_HOST_NAME as ATTR_HOST_NAME, ATTR_IP as ATTR_IP, ATTR_MAC as ATTR_MAC, ATTR_SOURCE_TYPE as ATTR_SOURCE_TYPE, CONNECTED_DEVICE_REGISTERED as CONNECTED_DEVICE_REGISTERED, SourceType as SourceType
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, STATE_HOME as STATE_HOME
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, format_mac as format_mac
from homeassistant.helpers.discovery_flow import DiscoveryKey as DiscoveryKey
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.event import async_track_state_added_domain as async_track_state_added_domain, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import DHCPMatcher as DHCPMatcher, async_get_dhcp as async_get_dhcp
from typing import Any, Final

CONFIG_SCHEMA: Incomplete
HOSTNAME: Final[str]
MAC_ADDRESS: Final[str]
IP_ADDRESS: Final[str]
REGISTERED_DEVICES: Final[str]
SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

@dataclass(slots=True)
class DhcpServiceInfo(BaseServiceInfo):
    ip: str
    hostname: str
    macaddress: str

@dataclass(slots=True)
class DhcpMatchers:
    registered_devices_domains: set[str]
    no_oui_matchers: dict[str, list[DHCPMatcher]]
    oui_matchers: dict[str, list[DHCPMatcher]]

def async_index_integration_matchers(integration_matchers: list[DHCPMatcher]) -> DhcpMatchers: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class WatcherBase:
    hass: Incomplete
    _integration_matchers: Incomplete
    _address_data: Incomplete
    _unsub: Callable[[], None] | None
    def __init__(self, hass: HomeAssistant, address_data: dict[str, dict[str, str]], integration_matchers: DhcpMatchers) -> None: ...
    @callback
    def async_stop(self) -> None: ...
    @callback
    def async_process_client(self, ip_address: str, hostname: str, unformatted_mac_address: str, force: bool = False) -> None: ...

class NetworkWatcher(WatcherBase):
    _discover_hosts: DiscoverHosts | None
    _discover_task: asyncio.Task | None
    def __init__(self, hass: HomeAssistant, address_data: dict[str, dict[str, str]], integration_matchers: DhcpMatchers) -> None: ...
    @callback
    def async_stop(self) -> None: ...
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...
    @callback
    def async_start_discover(self, *_: Any) -> None: ...
    async def async_discover(self) -> None: ...

class DeviceTrackerWatcher(WatcherBase):
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...
    @callback
    def _async_process_device_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_process_device_state(self, state: State | None) -> None: ...

class DeviceTrackerRegisteredWatcher(WatcherBase):
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...
    @callback
    def _async_process_device_data(self, data: dict[str, str | None]) -> None: ...

class DHCPWatcher(WatcherBase):
    @callback
    def _async_process_dhcp_request(self, response: aiodhcpwatcher.DHCPRequest) -> None: ...
    _unsub: Incomplete
    async def async_start(self) -> None: ...

class RediscoveryWatcher(WatcherBase):
    @callback
    def _handle_config_entry_removed(self, entry: config_entries.ConfigEntry) -> None: ...
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...

def _compile_fnmatch(pattern: str) -> re.Pattern: ...
def _memorized_fnmatch(name: str, pattern: str) -> bool: ...
