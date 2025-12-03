from .const import ATTR_CONNECTION as ATTR_CONNECTION, ATTR_DNSSEC as ATTR_DNSSEC, ATTR_ENCRYPTION as ATTR_ENCRYPTION, ATTR_IP_VERSIONS as ATTR_IP_VERSIONS, ATTR_PROTOCOLS as ATTR_PROTOCOLS, ATTR_SETTINGS as ATTR_SETTINGS, ATTR_STATUS as ATTR_STATUS, CONF_PROFILE_ID as CONF_PROFILE_ID, UPDATE_INTERVAL_ANALYTICS as UPDATE_INTERVAL_ANALYTICS, UPDATE_INTERVAL_CONNECTION as UPDATE_INTERVAL_CONNECTION, UPDATE_INTERVAL_SETTINGS as UPDATE_INTERVAL_SETTINGS
from .coordinator import NextDnsConnectionUpdateCoordinator as NextDnsConnectionUpdateCoordinator, NextDnsDnssecUpdateCoordinator as NextDnsDnssecUpdateCoordinator, NextDnsEncryptionUpdateCoordinator as NextDnsEncryptionUpdateCoordinator, NextDnsIpVersionsUpdateCoordinator as NextDnsIpVersionsUpdateCoordinator, NextDnsProtocolsUpdateCoordinator as NextDnsProtocolsUpdateCoordinator, NextDnsSettingsUpdateCoordinator as NextDnsSettingsUpdateCoordinator, NextDnsStatusUpdateCoordinator as NextDnsStatusUpdateCoordinator, NextDnsUpdateCoordinator as NextDnsUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from nextdns import AnalyticsDnssec as AnalyticsDnssec, AnalyticsEncryption as AnalyticsEncryption, AnalyticsIpVersions as AnalyticsIpVersions, AnalyticsProtocols as AnalyticsProtocols, AnalyticsStatus as AnalyticsStatus, ConnectionStatus as ConnectionStatus, Settings as Settings

type NextDnsConfigEntry = ConfigEntry[NextDnsData]
@dataclass
class NextDnsData:
    connection: NextDnsUpdateCoordinator[ConnectionStatus]
    dnssec: NextDnsUpdateCoordinator[AnalyticsDnssec]
    encryption: NextDnsUpdateCoordinator[AnalyticsEncryption]
    ip_versions: NextDnsUpdateCoordinator[AnalyticsIpVersions]
    protocols: NextDnsUpdateCoordinator[AnalyticsProtocols]
    settings: NextDnsUpdateCoordinator[Settings]
    status: NextDnsUpdateCoordinator[AnalyticsStatus]

PLATFORMS: Incomplete
COORDINATORS: list[tuple[str, type[NextDnsUpdateCoordinator], timedelta]]

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NextDnsConfigEntry) -> bool: ...
