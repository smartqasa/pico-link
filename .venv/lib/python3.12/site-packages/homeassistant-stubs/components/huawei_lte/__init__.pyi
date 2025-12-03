from .const import ADMIN_SERVICES as ADMIN_SERVICES, ALL_KEYS as ALL_KEYS, ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, CONF_MANUFACTURER as CONF_MANUFACTURER, CONF_UNAUTHENTICATED_MODE as CONF_UNAUTHENTICATED_MODE, CONNECTION_TIMEOUT as CONNECTION_TIMEOUT, DEFAULT_DEVICE_NAME as DEFAULT_DEVICE_NAME, DEFAULT_MANUFACTURER as DEFAULT_MANUFACTURER, DEFAULT_NOTIFY_SERVICE_NAME as DEFAULT_NOTIFY_SERVICE_NAME, DOMAIN as DOMAIN, KEY_DEVICE_BASIC_INFORMATION as KEY_DEVICE_BASIC_INFORMATION, KEY_DEVICE_INFORMATION as KEY_DEVICE_INFORMATION, KEY_DEVICE_SIGNAL as KEY_DEVICE_SIGNAL, KEY_DIALUP_MOBILE_DATASWITCH as KEY_DIALUP_MOBILE_DATASWITCH, KEY_LAN_HOST_INFO as KEY_LAN_HOST_INFO, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_MONTH_STATISTICS as KEY_MONITORING_MONTH_STATISTICS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_MONITORING_TRAFFIC_STATISTICS as KEY_MONITORING_TRAFFIC_STATISTICS, KEY_NET_CURRENT_PLMN as KEY_NET_CURRENT_PLMN, KEY_NET_NET_MODE as KEY_NET_NET_MODE, KEY_SMS_SMS_COUNT as KEY_SMS_SMS_COUNT, KEY_WLAN_HOST_LIST as KEY_WLAN_HOST_LIST, KEY_WLAN_WIFI_FEATURE_SWITCH as KEY_WLAN_WIFI_FEATURE_SWITCH, KEY_WLAN_WIFI_GUEST_NETWORK_SWITCH as KEY_WLAN_WIFI_GUEST_NETWORK_SWITCH, NOTIFY_SUPPRESS_TIMEOUT as NOTIFY_SUPPRESS_TIMEOUT, SERVICE_RESUME_INTEGRATION as SERVICE_RESUME_INTEGRATION, SERVICE_SUSPEND_INTEGRATION as SERVICE_SUSPEND_INTEGRATION, UPDATE_SIGNAL as UPDATE_SIGNAL
from .utils import get_device_macs as get_device_macs, non_verifying_requests_session as non_verifying_requests_session
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_RECIPIENT as CONF_RECIPIENT, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType
from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
from typing import Any, NamedTuple

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
NOTIFY_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_SCHEMA: Incomplete
PLATFORMS: Incomplete

@dataclass
class Router:
    hass: HomeAssistant
    config_entry: ConfigEntry
    connection: Connection
    url: str
    data: dict[str, Any] = field(default_factory=dict, init=False)
    subscriptions: dict[str, list[str]] = field(default_factory=Incomplete, init=False)
    inflight_gets: set[str] = field(default_factory=set, init=False)
    client: Client = field(init=False)
    suspended: bool = field(default=False, init=False)
    notify_last_attempt: float = field(default=None, init=False)
    def __post_init__(self) -> None: ...
    @property
    def device_name(self) -> str: ...
    @property
    def device_identifiers(self) -> set[tuple[str, str]]: ...
    @property
    def device_connections(self) -> set[tuple[str, str]]: ...
    def _get_data(self, key: str, func: Callable[[], Any]) -> None: ...
    def update(self) -> None: ...
    def logout(self) -> None: ...
    def cleanup(self, *_: Any) -> None: ...

class HuaweiLteData(NamedTuple):
    hass_config: ConfigType
    routers: dict[str, Router]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
