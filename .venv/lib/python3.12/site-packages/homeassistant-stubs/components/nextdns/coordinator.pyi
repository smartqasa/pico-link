from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from nextdns import AnalyticsDnssec, AnalyticsEncryption, AnalyticsIpVersions, AnalyticsProtocols, AnalyticsStatus, ConnectionStatus, NextDns as NextDns, Settings
from nextdns.model import NextDnsData
from typing import TypeVar

_LOGGER: Incomplete
CoordinatorDataT = TypeVar('CoordinatorDataT', bound=NextDnsData)

class NextDnsUpdateCoordinator(DataUpdateCoordinator[CoordinatorDataT]):
    nextdns: Incomplete
    profile_id: Incomplete
    profile_name: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, nextdns: NextDns, profile_id: str, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> CoordinatorDataT: ...
    async def _async_update_data_internal(self) -> CoordinatorDataT: ...

class NextDnsStatusUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsStatus]):
    async def _async_update_data_internal(self) -> AnalyticsStatus: ...

class NextDnsDnssecUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsDnssec]):
    async def _async_update_data_internal(self) -> AnalyticsDnssec: ...

class NextDnsEncryptionUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsEncryption]):
    async def _async_update_data_internal(self) -> AnalyticsEncryption: ...

class NextDnsIpVersionsUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsIpVersions]):
    async def _async_update_data_internal(self) -> AnalyticsIpVersions: ...

class NextDnsProtocolsUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsProtocols]):
    async def _async_update_data_internal(self) -> AnalyticsProtocols: ...

class NextDnsSettingsUpdateCoordinator(NextDnsUpdateCoordinator[Settings]):
    async def _async_update_data_internal(self) -> Settings: ...

class NextDnsConnectionUpdateCoordinator(NextDnsUpdateCoordinator[ConnectionStatus]):
    async def _async_update_data_internal(self) -> ConnectionStatus: ...
