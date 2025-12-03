import asyncio
from .addon import get_addon_manager as get_addon_manager
from .api import async_register_api as async_register_api
from .const import ATTR_ACKNOWLEDGED_FRAMES as ATTR_ACKNOWLEDGED_FRAMES, ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_COMMAND_CLASS_NAME as ATTR_COMMAND_CLASS_NAME, ATTR_DATA_TYPE as ATTR_DATA_TYPE, ATTR_DATA_TYPE_LABEL as ATTR_DATA_TYPE_LABEL, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_EVENT as ATTR_EVENT, ATTR_EVENT_DATA as ATTR_EVENT_DATA, ATTR_EVENT_LABEL as ATTR_EVENT_LABEL, ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, ATTR_EVENT_TYPE_LABEL as ATTR_EVENT_TYPE_LABEL, ATTR_HOME_ID as ATTR_HOME_ID, ATTR_LABEL as ATTR_LABEL, ATTR_NODE_ID as ATTR_NODE_ID, ATTR_PARAMETERS as ATTR_PARAMETERS, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_PROPERTY_KEY_NAME as ATTR_PROPERTY_KEY_NAME, ATTR_PROPERTY_NAME as ATTR_PROPERTY_NAME, ATTR_STATUS as ATTR_STATUS, ATTR_TEST_NODE_ID as ATTR_TEST_NODE_ID, ATTR_TYPE as ATTR_TYPE, ATTR_VALUE as ATTR_VALUE, ATTR_VALUE_RAW as ATTR_VALUE_RAW, CONF_ADDON_DEVICE as CONF_ADDON_DEVICE, CONF_ADDON_LR_S2_ACCESS_CONTROL_KEY as CONF_ADDON_LR_S2_ACCESS_CONTROL_KEY, CONF_ADDON_LR_S2_AUTHENTICATED_KEY as CONF_ADDON_LR_S2_AUTHENTICATED_KEY, CONF_ADDON_NETWORK_KEY as CONF_ADDON_NETWORK_KEY, CONF_ADDON_S0_LEGACY_KEY as CONF_ADDON_S0_LEGACY_KEY, CONF_ADDON_S2_ACCESS_CONTROL_KEY as CONF_ADDON_S2_ACCESS_CONTROL_KEY, CONF_ADDON_S2_AUTHENTICATED_KEY as CONF_ADDON_S2_AUTHENTICATED_KEY, CONF_ADDON_S2_UNAUTHENTICATED_KEY as CONF_ADDON_S2_UNAUTHENTICATED_KEY, CONF_DATA_COLLECTION_OPTED_IN as CONF_DATA_COLLECTION_OPTED_IN, CONF_INSTALLER_MODE as CONF_INSTALLER_MODE, CONF_INTEGRATION_CREATED_ADDON as CONF_INTEGRATION_CREATED_ADDON, CONF_LR_S2_ACCESS_CONTROL_KEY as CONF_LR_S2_ACCESS_CONTROL_KEY, CONF_LR_S2_AUTHENTICATED_KEY as CONF_LR_S2_AUTHENTICATED_KEY, CONF_NETWORK_KEY as CONF_NETWORK_KEY, CONF_S0_LEGACY_KEY as CONF_S0_LEGACY_KEY, CONF_S2_ACCESS_CONTROL_KEY as CONF_S2_ACCESS_CONTROL_KEY, CONF_S2_AUTHENTICATED_KEY as CONF_S2_AUTHENTICATED_KEY, CONF_S2_UNAUTHENTICATED_KEY as CONF_S2_UNAUTHENTICATED_KEY, CONF_USB_PATH as CONF_USB_PATH, CONF_USE_ADDON as CONF_USE_ADDON, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, EVENT_DEVICE_ADDED_TO_REGISTRY as EVENT_DEVICE_ADDED_TO_REGISTRY, EVENT_VALUE_UPDATED as EVENT_VALUE_UPDATED, LIB_LOGGER as LIB_LOGGER, LOGGER as LOGGER, LR_ADDON_VERSION as LR_ADDON_VERSION, USER_AGENT as USER_AGENT, ZWAVE_JS_NOTIFICATION_EVENT as ZWAVE_JS_NOTIFICATION_EVENT, ZWAVE_JS_VALUE_NOTIFICATION_EVENT as ZWAVE_JS_VALUE_NOTIFICATION_EVENT, ZWAVE_JS_VALUE_UPDATED_EVENT as ZWAVE_JS_VALUE_UPDATED_EVENT
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo, async_discover_node_values as async_discover_node_values, async_discover_single_value as async_discover_single_value
from .helpers import async_disable_server_logging_if_needed as async_disable_server_logging_if_needed, async_enable_server_logging_if_needed as async_enable_server_logging_if_needed, async_enable_statistics as async_enable_statistics, get_device_id as get_device_id, get_device_id_ext as get_device_id_ext, get_network_identifier_for_notification as get_network_identifier_for_notification, get_unique_id as get_unique_id, get_valueless_base_unique_id as get_valueless_base_unique_id
from .migrate import async_migrate_discovered_value as async_migrate_discovered_value
from .services import ZWaveServices as ZWaveServices
from _typeshed import Incomplete
from homeassistant.components.hassio import AddonError as AddonError, AddonManager as AddonManager, AddonState as AddonState
from homeassistant.components.persistent_notification import async_create as async_create
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_DOMAIN as ATTR_DOMAIN, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_URL as CONF_URL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_LOGGING_CHANGED as EVENT_LOGGING_CHANGED, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, UNDEFINED as UNDEFINED
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import Value as Value, ValueNotification as ValueNotification

CONNECT_TIMEOUT: int
DATA_CLIENT_LISTEN_TASK: str
DATA_DRIVER_EVENTS: str
DATA_START_CLIENT_TASK: str
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def start_client(hass: HomeAssistant, entry: ConfigEntry, client: ZwaveClient) -> None: ...

class DriverEvents:
    driver: Driver
    config_entry: Incomplete
    dev_reg: Incomplete
    hass: Incomplete
    platform_setup_tasks: dict[str, asyncio.Task]
    ready: Incomplete
    controller_events: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def setup(self, driver: Driver) -> None: ...
    async def async_setup_platform(self, platform: Platform) -> None: ...

class ControllerEvents:
    hass: Incomplete
    config_entry: Incomplete
    discovered_value_ids: dict[str, set[str]]
    driver_events: Incomplete
    dev_reg: Incomplete
    registered_unique_ids: dict[str, dict[Platform, set[str]]]
    node_events: Incomplete
    def __init__(self, hass: HomeAssistant, driver_events: DriverEvents) -> None: ...
    @callback
    def remove_device(self, device: dr.DeviceEntry) -> None: ...
    async def async_on_node_added(self, node: ZwaveNode) -> None: ...
    @callback
    def async_on_node_removed(self, event: dict) -> None: ...
    @callback
    def async_on_identify(self, event: dict) -> None: ...
    @callback
    def register_node_in_dev_reg(self, node: ZwaveNode) -> dr.DeviceEntry: ...

class NodeEvents:
    config_entry: Incomplete
    controller_events: Incomplete
    dev_reg: Incomplete
    ent_reg: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, controller_events: ControllerEvents) -> None: ...
    async def async_on_node_ready(self, node: ZwaveNode) -> None: ...
    async def async_handle_discovery_info(self, device: dr.DeviceEntry, disc_info: ZwaveDiscoveryInfo, value_updates_disc_info: dict[str, ZwaveDiscoveryInfo]) -> None: ...
    async def async_on_value_added(self, value_updates_disc_info: dict[str, ZwaveDiscoveryInfo], value: Value) -> None: ...
    @callback
    def async_on_value_notification(self, notification: ValueNotification) -> None: ...
    @callback
    def async_on_notification(self, event: dict[str, Any]) -> None: ...
    @callback
    def async_on_value_updated_fire_event(self, value_updates_disc_info: dict[str, ZwaveDiscoveryInfo], value: Value) -> None: ...

async def client_listen(hass: HomeAssistant, entry: ConfigEntry, client: ZwaveClient, driver_ready: asyncio.Event) -> None: ...
async def disconnect_client(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
async def async_ensure_addon_running(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
@callback
def _get_addon_manager(hass: HomeAssistant) -> AddonManager: ...
