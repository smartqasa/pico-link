from .bluetooth import async_connect_scanner as async_connect_scanner
from .const import CONF_ALLOW_SERVICE_CALLS as CONF_ALLOW_SERVICE_CALLS, CONF_DEVICE_NAME as CONF_DEVICE_NAME, DEFAULT_ALLOW_SERVICE_CALLS as DEFAULT_ALLOW_SERVICE_CALLS, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN, PROJECT_URLS as PROJECT_URLS, STABLE_BLE_VERSION as STABLE_BLE_VERSION, STABLE_BLE_VERSION_STR as STABLE_BLE_VERSION_STR
from .dashboard import async_get_dashboard as async_get_dashboard
from .domain_data import DomainData as DomainData
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, APIVersion as APIVersion, DeviceInfo as EsphomeDeviceInfo, EntityInfo as EntityInfo, HomeassistantServiceCall as HomeassistantServiceCall, ReconnectLogic, UserService as UserService
from homeassistant.components import tag as tag, zeroconf as zeroconf
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_MODE as CONF_MODE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_LOGGING_CHANGED as EVENT_LOGGING_CHANGED, Platform as Platform
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers import template as template
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.template import Template as Template
from homeassistant.util.async_ import create_eager_task as create_eager_task
from typing import Any, NamedTuple

_LOGGER: Incomplete

@callback
def _async_check_firmware_version(hass: HomeAssistant, device_info: EsphomeDeviceInfo, api_version: APIVersion) -> None: ...
@callback
def _async_check_using_api_password(hass: HomeAssistant, device_info: EsphomeDeviceInfo, has_password: bool) -> None: ...

class ESPHomeManager:
    __slots__: Incomplete
    hass: Incomplete
    host: Incomplete
    password: Incomplete
    entry: Incomplete
    cli: Incomplete
    device_id: str | None
    domain_data: Incomplete
    reconnect_logic: ReconnectLogic | None
    zeroconf_instance: Incomplete
    entry_data: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ESPHomeConfigEntry, host: str, password: str | None, cli: APIClient, zeroconf_instance: zeroconf.HaZeroconf, domain_data: DomainData) -> None: ...
    async def on_stop(self, event: Event) -> None: ...
    @property
    def services_issue(self) -> str: ...
    @callback
    def async_on_service_call(self, service: HomeassistantServiceCall) -> None: ...
    @callback
    def _send_home_assistant_state(self, entity_id: str, attribute: str | None, state: State | None) -> None: ...
    @callback
    def _send_home_assistant_state_event(self, attribute: str | None, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def async_on_state_subscription(self, entity_id: str, attribute: str | None = None) -> None: ...
    @callback
    def async_on_state_request(self, entity_id: str, attribute: str | None = None) -> None: ...
    async def on_connect(self) -> None: ...
    async def _on_connnect(self) -> None: ...
    async def on_disconnect(self, expected_disconnect: bool) -> None: ...
    async def on_connect_error(self, err: Exception) -> None: ...
    @callback
    def _async_handle_logging_changed(self, _event: Event) -> None: ...
    async def async_start(self) -> None: ...

@callback
def _async_setup_device_registry(hass: HomeAssistant, entry: ESPHomeConfigEntry, entry_data: RuntimeEntryData) -> str: ...

class ServiceMetadata(NamedTuple):
    validator: Any
    example: str
    selector: dict[str, Any]
    description: str | None = ...

ARG_TYPE_METADATA: Incomplete

@callback
def execute_service(entry_data: RuntimeEntryData, service: UserService, call: ServiceCall) -> None: ...
def build_service_name(device_info: EsphomeDeviceInfo, service: UserService) -> str: ...
@callback
def _async_register_service(hass: HomeAssistant, entry_data: RuntimeEntryData, device_info: EsphomeDeviceInfo, service: UserService) -> None: ...
@callback
def _setup_services(hass: HomeAssistant, entry_data: RuntimeEntryData, services: list[UserService]) -> None: ...
async def cleanup_instance(hass: HomeAssistant, entry: ESPHomeConfigEntry) -> RuntimeEntryData: ...
