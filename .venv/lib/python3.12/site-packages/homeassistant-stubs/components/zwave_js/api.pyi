import homeassistant.helpers.device_registry as dr
from .config_validation import BITMASK_SCHEMA as BITMASK_SCHEMA
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_METHOD_NAME as ATTR_METHOD_NAME, ATTR_PARAMETERS as ATTR_PARAMETERS, ATTR_WAIT_FOR_RESULT as ATTR_WAIT_FOR_RESULT, CONF_DATA_COLLECTION_OPTED_IN as CONF_DATA_COLLECTION_OPTED_IN, CONF_INSTALLER_MODE as CONF_INSTALLER_MODE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, EVENT_DEVICE_ADDED_TO_REGISTRY as EVENT_DEVICE_ADDED_TO_REGISTRY, USER_AGENT as USER_AGENT
from .helpers import async_enable_statistics as async_enable_statistics, async_get_node_from_device_id as async_get_node_from_device_id, get_device_id as get_device_id
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection, ERR_INVALID_FORMAT as ERR_INVALID_FORMAT, ERR_NOT_FOUND as ERR_NOT_FOUND, ERR_NOT_SUPPORTED as ERR_NOT_SUPPORTED, ERR_UNKNOWN_ERROR as ERR_UNKNOWN_ERROR
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from typing import Any, Concatenate, Literal
from zwave_js_server.client import Client as Client
from zwave_js_server.const import InclusionStrategy
from zwave_js_server.model.controller import ControllerStatistics as ControllerStatistics
from zwave_js_server.model.controller.firmware import ControllerFirmwareUpdateProgress as ControllerFirmwareUpdateProgress, ControllerFirmwareUpdateResult as ControllerFirmwareUpdateResult
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.endpoint import Endpoint as Endpoint
from zwave_js_server.model.log_message import LogMessage as LogMessage
from zwave_js_server.model.node import Node as Node, NodeStatistics as NodeStatistics
from zwave_js_server.model.node.firmware import NodeFirmwareUpdateProgress as NodeFirmwareUpdateProgress, NodeFirmwareUpdateResult as NodeFirmwareUpdateResult

DATA_UNSUBSCRIBE: str
ID: str
ENTRY_ID: str
ERR_NOT_LOADED: str
NODE_ID: str
DEVICE_ID: str
COMMAND_CLASS_ID: str
TYPE: str
PROPERTY: str
PROPERTY_KEY: str
ENDPOINT: str
VALUE: str
VALUE_SIZE: str
VALUE_FORMAT: str
CONFIG: str
LEVEL: str
LOG_TO_FILE: str
FILENAME: str
ENABLED: str
FORCE_CONSOLE: str
VALUE_ID: str
STATUS: str
OPTED_IN: str
SECURITY_CLASSES: str
CLIENT_SIDE_AUTH: str
INCLUSION_STRATEGY: str
INCLUSION_STRATEGY_NOT_SMART_START: dict[int, Literal[InclusionStrategy.DEFAULT, InclusionStrategy.SECURITY_S0, InclusionStrategy.SECURITY_S2, InclusionStrategy.INSECURE]]
PIN: str
FORCE_SECURITY: str
PLANNED_PROVISIONING_ENTRY: str
QR_PROVISIONING_INFORMATION: str
QR_CODE_STRING: str
DSK: str
VERSION: str
GENERIC_DEVICE_CLASS: str
SPECIFIC_DEVICE_CLASS: str
INSTALLER_ICON_TYPE: str
MANUFACTURER_ID: str
PRODUCT_TYPE: str
PRODUCT_ID: str
APPLICATION_VERSION: str
MAX_INCLUSION_REQUEST_INTERVAL: str
UUID: str
SUPPORTED_PROTOCOLS: str
ADDITIONAL_PROPERTIES: str
REQUESTED_SECURITY_CLASSES: str
FEATURE: str
STRATEGY: str
MINIMUM_QR_STRING_LENGTH: int
PLANNED_PROVISIONING_ENTRY_SCHEMA: Incomplete
QR_PROVISIONING_INFORMATION_SCHEMA: Incomplete
QR_CODE_STRING_SCHEMA: Incomplete

async def _async_get_entry(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry_id: str) -> tuple[ConfigEntry, Client, Driver] | tuple[None, None, None]: ...
def async_get_entry(orig_func: Callable[[HomeAssistant, ActiveConnection, dict[str, Any], ConfigEntry, Client, Driver], Coroutine[Any, Any, None]]) -> Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Coroutine[Any, Any, None]]: ...
async def _async_get_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict, device_id: str) -> Node | None: ...
def async_get_node(orig_func: Callable[[HomeAssistant, ActiveConnection, dict[str, Any], Node], Coroutine[Any, Any, None]]) -> Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Coroutine[Any, Any, None]]: ...
def async_handle_failed_command[**_P](orig_func: Callable[Concatenate[HomeAssistant, ActiveConnection, dict[str, Any], _P], Coroutine[Any, Any, None]]) -> Callable[Concatenate[HomeAssistant, ActiveConnection, dict[str, Any], _P], Coroutine[Any, Any, None]]: ...
def node_status(node: Node) -> dict[str, Any]: ...
@callback
def async_register_api(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_network_status(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@async_get_node
async def websocket_subscribe_node_status(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.async_response
@async_get_node
async def websocket_node_status(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.async_response
@async_get_node
async def websocket_node_metadata(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.async_response
@async_get_node
async def websocket_node_alerts(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_add_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_cancel_secure_bootstrap_s2(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_subscribe_s2_inclusion(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_grant_security_classes(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_validate_dsk_and_enter_pin(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_provision_smart_start_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_unprovision_smart_start_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_get_provisioning_entries(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_parse_qr_code_string(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_try_parse_dsk_from_qr_code_string(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_supports_feature(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_stop_inclusion(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_stop_exclusion(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_remove_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_replace_failed_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_remove_failed_node(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_begin_rebuilding_routes(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_entry
async def websocket_subscribe_rebuild_routes_progress(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_stop_rebuilding_routes(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_rebuild_node_routes(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_refresh_node_info(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_refresh_node_values(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_refresh_node_cc_values(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_set_config_parameter(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_node
async def websocket_get_config_parameters(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_set_raw_config_parameter(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_get_raw_config_parameter(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
def filename_is_present_if_logging_to_file(obj: dict) -> dict: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_subscribe_log_updates(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_update_log_config(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_entry
async def websocket_get_log_config(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_update_data_collection_preference(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_data_collection_status(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_abort_firmware_update(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_is_node_firmware_update_in_progress(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
def _get_node_firmware_update_progress_dict(progress: NodeFirmwareUpdateProgress) -> dict[str, int | float]: ...
def _get_controller_firmware_update_progress_dict(progress: ControllerFirmwareUpdateProgress) -> dict[str, int | float]: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_node
async def websocket_subscribe_firmware_update_status(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_get_node_firmware_update_capabilities(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_is_any_ota_firmware_update_in_progress(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...

class FirmwareUploadView(HomeAssistantView):
    url: str
    name: str
    _dev_reg: Incomplete
    def __init__(self, dev_reg: dr.DeviceRegistry) -> None: ...
    @require_admin
    async def post(self, request: web.Request, device_id: str) -> web.Response: ...

@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_check_for_config_updates(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_install_config_update(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
def _get_controller_statistics_dict(statistics: ControllerStatistics) -> dict[str, int]: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_entry
async def websocket_subscribe_controller_statistics(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
def _get_node_statistics_dict(hass: HomeAssistant, statistics: NodeStatistics) -> dict[str, Any]: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_get_node
async def websocket_subscribe_node_statistics(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_entry
async def websocket_hard_reset_controller(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], entry: ConfigEntry, client: Client, driver: Driver) -> None: ...
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_node_capabilities(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@async_handle_failed_command
@async_get_node
async def websocket_invoke_cc_api(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], node: Node) -> None: ...
@callback
@websocket_api.require_admin
def websocket_get_integration_settings(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
