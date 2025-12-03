from . import type_cameras as type_cameras, type_covers as type_covers, type_fans as type_fans, type_humidifiers as type_humidifiers, type_lights as type_lights, type_locks as type_locks, type_media_players as type_media_players, type_remotes as type_remotes, type_security_systems as type_security_systems, type_sensors as type_sensors, type_switches as type_switches, type_thermostats as type_thermostats
from .accessories import HomeAccessory as HomeAccessory, HomeBridge as HomeBridge, HomeDriver as HomeDriver, get_accessory as get_accessory
from .aidmanager import AccessoryAidStorage as AccessoryAidStorage
from .const import ATTR_INTEGRATION as ATTR_INTEGRATION, BRIDGE_NAME as BRIDGE_NAME, BRIDGE_SERIAL_NUMBER as BRIDGE_SERIAL_NUMBER, CONFIG_OPTIONS as CONFIG_OPTIONS, CONF_ADVERTISE_IP as CONF_ADVERTISE_IP, CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_ENTRY_INDEX as CONF_ENTRY_INDEX, CONF_EXCLUDE_ACCESSORY_MODE as CONF_EXCLUDE_ACCESSORY_MODE, CONF_FILTER as CONF_FILTER, CONF_HOMEKIT_MODE as CONF_HOMEKIT_MODE, CONF_LINKED_BATTERY_CHARGING_SENSOR as CONF_LINKED_BATTERY_CHARGING_SENSOR, CONF_LINKED_BATTERY_SENSOR as CONF_LINKED_BATTERY_SENSOR, CONF_LINKED_DOORBELL_SENSOR as CONF_LINKED_DOORBELL_SENSOR, CONF_LINKED_HUMIDITY_SENSOR as CONF_LINKED_HUMIDITY_SENSOR, CONF_LINKED_MOTION_SENSOR as CONF_LINKED_MOTION_SENSOR, DEFAULT_EXCLUDE_ACCESSORY_MODE as DEFAULT_EXCLUDE_ACCESSORY_MODE, DEFAULT_HOMEKIT_MODE as DEFAULT_HOMEKIT_MODE, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, HOMEKIT_MODES as HOMEKIT_MODES, HOMEKIT_MODE_ACCESSORY as HOMEKIT_MODE_ACCESSORY, MANUFACTURER as MANUFACTURER, PERSIST_LOCK_DATA as PERSIST_LOCK_DATA, SERVICE_HOMEKIT_RESET_ACCESSORY as SERVICE_HOMEKIT_RESET_ACCESSORY, SERVICE_HOMEKIT_UNPAIR as SERVICE_HOMEKIT_UNPAIR, SHUTDOWN_TIMEOUT as SHUTDOWN_TIMEOUT, SIGNAL_RELOAD_ENTITIES as SIGNAL_RELOAD_ENTITIES
from .iidmanager import AccessoryIIDStorage as AccessoryIIDStorage
from .models import HomeKitConfigEntry as HomeKitConfigEntry, HomeKitEntryData as HomeKitEntryData
from .type_triggers import DeviceTriggerAccessory as DeviceTriggerAccessory
from .util import accessory_friendly_name as accessory_friendly_name, async_dismiss_setup_message as async_dismiss_setup_message, async_port_is_available as async_port_is_available, async_show_setup_message as async_show_setup_message, get_persist_fullpath_for_entry_id as get_persist_fullpath_for_entry_id, remove_state_files_for_entry_id as remove_state_files_for_entry_id, state_needs_accessory_mode as state_needs_accessory_mode, validate_entity_config as validate_entity_config
from _typeshed import Incomplete
from aiohttp import web
from collections import defaultdict
from collections.abc import Iterable
from homeassistant.components import device_automation as device_automation, network as network, zeroconf as zeroconf
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.device_automation.trigger import async_validate_trigger_config as async_validate_trigger_config
from homeassistant.components.event import EventDeviceClass as EventDeviceClass
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_DEVICES as CONF_DEVICES, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized
from homeassistant.helpers import device_registry as dr, entity_registry as er, instance_id as instance_id
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entityfilter import BASE_FILTER_SCHEMA as BASE_FILTER_SCHEMA, EntityFilter as EntityFilter, FILTER_SCHEMA as FILTER_SCHEMA
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.service import async_extract_referenced_entity_ids as async_extract_referenced_entity_ids, async_register_admin_service as async_register_admin_service
from homeassistant.helpers.start import async_at_started as async_at_started
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from homeassistant.util.async_ import create_eager_task as create_eager_task
from pyhap.characteristic import Characteristic as Characteristic
from pyhap.service import Service as Service
from typing import Any
from zeroconf.asyncio import AsyncZeroconf as AsyncZeroconf

_LOGGER: Incomplete
MAX_DEVICES: int
STATUS_READY: int
STATUS_RUNNING: int
STATUS_STOPPED: int
STATUS_WAIT: int
PORT_CLEANUP_CHECK_INTERVAL_SECS: int
_HOMEKIT_CONFIG_UPDATE_TIME: int
_HAS_IPV6: Incomplete
_DEFAULT_BIND: Incomplete
BATTERY_CHARGING_SENSOR: Incomplete
BATTERY_SENSOR: Incomplete
MOTION_EVENT_SENSOR: Incomplete
MOTION_SENSOR: Incomplete
DOORBELL_EVENT_SENSOR: Incomplete
HUMIDITY_SENSOR: Incomplete

def _has_all_unique_names_and_ports(bridges: list[dict[str, Any]]) -> list[dict[str, Any]]: ...

BRIDGE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
RESET_ACCESSORY_SERVICE_SCHEMA: Incomplete
UNPAIR_SERVICE_SCHEMA: Incomplete

def _async_all_homekit_instances(hass: HomeAssistant) -> list[HomeKit]: ...
def _async_get_imported_entries_indices(current_entries: list[ConfigEntry]) -> tuple[dict[str, ConfigEntry], dict[int, ConfigEntry]]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _async_update_config_entry_from_yaml(hass: HomeAssistant, entries_by_name: dict[str, ConfigEntry], entries_by_port: dict[int, ConfigEntry], conf: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeKitConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: HomeKitConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: HomeKitConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: HomeKitConfigEntry) -> None: ...
@callback
def _async_import_options_from_data_if_missing(hass: HomeAssistant, entry: HomeKitConfigEntry) -> None: ...
@callback
def _async_register_events_and_services(hass: HomeAssistant) -> None: ...

class HomeKit:
    hass: Incomplete
    _name: Incomplete
    _port: Incomplete
    _ip_address: Incomplete
    _filter: Incomplete
    _config: defaultdict[str, dict[str, Any]]
    _exclude_accessory_mode: Incomplete
    _advertise_ips: Incomplete
    _entry_id: Incomplete
    _entry_title: Incomplete
    _homekit_mode: Incomplete
    _devices: Incomplete
    aid_storage: AccessoryAidStorage | None
    iid_storage: AccessoryIIDStorage | None
    status: Incomplete
    driver: HomeDriver | None
    bridge: HomeBridge | None
    _reset_lock: Incomplete
    _cancel_reload_dispatcher: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant, name: str, port: int, ip_address: str | None, entity_filter: EntityFilter, exclude_accessory_mode: bool, entity_config: dict[str, Any], homekit_mode: str, advertise_ips: list[str], entry_id: str, entry_title: str, devices: list[str] | None = None) -> None: ...
    def setup(self, async_zeroconf_instance: AsyncZeroconf, uuid: str) -> bool: ...
    async def async_reset_accessories(self, entity_ids: Iterable[str]) -> None: ...
    async def async_reload_accessories(self, entity_ids: Iterable[str]) -> None: ...
    @callback
    def _async_shutdown_accessory(self, accessory: HomeAccessory) -> None: ...
    async def _async_reload_accessories_in_accessory_mode(self, entity_ids: Iterable[str]) -> None: ...
    def _async_remove_accessories_by_entity_id(self, entity_ids: Iterable[str]) -> list[str]: ...
    async def _async_reset_accessories_in_bridge_mode(self, entity_ids: Iterable[str]) -> None: ...
    async def _async_reload_accessories_in_bridge_mode(self, entity_ids: Iterable[str]) -> None: ...
    async def _async_recreate_removed_accessories_in_bridge_mode(self, removed: list[str]) -> None: ...
    @callback
    def _async_update_accessories_hash(self) -> bool: ...
    def add_bridge_accessory(self, state: State) -> HomeAccessory | None: ...
    def _would_exceed_max_devices(self, name: str | None) -> bool: ...
    async def add_bridge_triggers_accessory(self, device: dr.DeviceEntry, device_triggers: list[dict[str, Any]]) -> None: ...
    @callback
    def async_remove_bridge_accessory(self, aid: int) -> HomeAccessory | None: ...
    async def async_configure_accessories(self) -> list[State]: ...
    async def async_start(self, *args: Any) -> None: ...
    @callback
    def _async_show_setup_message(self) -> None: ...
    @callback
    def async_unpair(self) -> None: ...
    @callback
    def _async_register_bridge(self) -> None: ...
    @callback
    def _async_purge_old_bridges(self, dev_reg: dr.DeviceRegistry, identifier: tuple[str, str, str], connection: tuple[str, str]) -> None: ...
    @callback
    def _async_create_single_accessory(self, entity_states: list[State]) -> HomeAccessory | None: ...
    async def _async_create_bridge_accessory(self, entity_states: Iterable[State]) -> HomeAccessory: ...
    async def _async_add_trigger_accessories(self) -> None: ...
    async def _async_create_accessories(self) -> bool: ...
    async def async_stop(self, *args: Any) -> None: ...
    @callback
    def _async_configure_linked_sensors(self, ent_reg_ent: er.RegistryEntry, lookup: dict[tuple[str, str | None], str], state: State) -> None: ...
    async def _async_set_device_info_attributes(self, ent_reg_ent: er.RegistryEntry, dev_reg: dr.DeviceRegistry, entity_id: str) -> None: ...
    def _fill_config_from_device_registry_entry(self, device_entry: dr.DeviceEntry, config: dict[str, Any]) -> None: ...

class HomeKitPairingQRView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    async def get(self, request: web.Request) -> web.Response: ...
