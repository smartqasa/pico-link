from . import entity_registry as entity_registry, storage as storage, translation as translation
from .debounce import Debouncer as Debouncer
from .frame import ReportBehavior as ReportBehavior, report_usage as report_usage
from .json import JSON_DUMP as JSON_DUMP, find_paths_unserializable_data as find_paths_unserializable_data, json_bytes as json_bytes, json_fragment as json_fragment
from .registry import BaseRegistry as BaseRegistry, BaseRegistryItems as BaseRegistryItems, RegistryIndexType as RegistryIndexType
from .singleton import singleton as singleton
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Mapping
from datetime import datetime
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ReleaseChannel as ReleaseChannel, callback as callback, get_release_channel as get_release_channel
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp, utcnow as utcnow
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.json import format_unserializable_data as format_unserializable_data
from propcache import cached_property as under_cached_property
from typing import Any, Literal, TypedDict
from yarl import URL

_LOGGER: Incomplete
DATA_REGISTRY: HassKey[DeviceRegistry]
EVENT_DEVICE_REGISTRY_UPDATED: EventType[EventDeviceRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int
CLEANUP_DELAY: int
CONNECTION_BLUETOOTH: str
CONNECTION_NETWORK_MAC: str
CONNECTION_UPNP: str
CONNECTION_ZIGBEE: str
ORPHANED_DEVICE_KEEP_SECONDS: Incomplete
RUNTIME_ONLY_ATTRS: Incomplete
CONFIGURATION_URL_SCHEMES: Incomplete

class DeviceEntryDisabler(StrEnum):
    CONFIG_ENTRY = 'config_entry'
    INTEGRATION = 'integration'
    USER = 'user'

class DeviceInfo(TypedDict, total=False):
    configuration_url: str | URL | None
    connections: set[tuple[str, str]]
    created_at: str
    default_manufacturer: str
    default_model: str
    default_name: str
    entry_type: DeviceEntryType | None
    identifiers: set[tuple[str, str]]
    manufacturer: str | None
    model: str | None
    model_id: str | None
    modified_at: str
    name: str | None
    serial_number: str | None
    suggested_area: str | None
    sw_version: str | None
    hw_version: str | None
    translation_key: str | None
    translation_placeholders: Mapping[str, str] | None
    via_device: tuple[str, str]

DEVICE_INFO_TYPES: Incomplete
DEVICE_INFO_KEYS: Incomplete
LOW_PRIO_CONFIG_ENTRY_DOMAINS: Incomplete

class _EventDeviceRegistryUpdatedData_CreateRemove(TypedDict):
    action: Literal['create', 'remove']
    device_id: str

class _EventDeviceRegistryUpdatedData_Update(TypedDict):
    action: Literal['update']
    device_id: str
    changes: dict[str, Any]
type EventDeviceRegistryUpdatedData = _EventDeviceRegistryUpdatedData_CreateRemove | _EventDeviceRegistryUpdatedData_Update

class DeviceEntryType(StrEnum):
    SERVICE = 'service'

class DeviceInfoError(HomeAssistantError):
    device_info: Incomplete
    domain: Incomplete
    def __init__(self, domain: str, device_info: DeviceInfo, message: str) -> None: ...

class DeviceCollisionError(HomeAssistantError): ...

class DeviceIdentifierCollisionError(DeviceCollisionError):
    def __init__(self, identifiers: set[tuple[str, str]], existing_device: DeviceEntry) -> None: ...

class DeviceConnectionCollisionError(DeviceCollisionError):
    def __init__(self, normalized_connections: set[tuple[str, str]], existing_device: DeviceEntry) -> None: ...

def _validate_device_info(config_entry: ConfigEntry, device_info: DeviceInfo) -> str: ...

_cached_parse_url: Incomplete

def _validate_configuration_url(value: Any) -> str | None: ...

class DeviceEntry:
    area_id: str | None
    config_entries: set[str]
    configuration_url: str | None
    connections: set[tuple[str, str]]
    created_at: datetime
    disabled_by: DeviceEntryDisabler | None
    entry_type: DeviceEntryType | None
    hw_version: str | None
    id: str
    identifiers: set[tuple[str, str]]
    labels: set[str]
    manufacturer: str | None
    model: str | None
    model_id: str | None
    modified_at: datetime
    name_by_user: str | None
    name: str | None
    primary_config_entry: str | None
    serial_number: str | None
    suggested_area: str | None
    sw_version: str | None
    via_device_id: str | None
    is_new: bool
    _cache: dict[str, Any]
    @property
    def disabled(self) -> bool: ...
    @property
    def dict_repr(self) -> dict[str, Any]: ...
    @under_cached_property
    def json_repr(self) -> bytes | None: ...
    @under_cached_property
    def as_storage_fragment(self) -> json_fragment: ...
    def __init__(self, area_id, config_entries, configuration_url, connections, created_at, disabled_by, entry_type, hw_version, id, identifiers, labels, manufacturer, model, model_id, modified_at, name_by_user, name, primary_config_entry, serial_number, suggested_area, sw_version, via_device_id, is_new, cache) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class DeletedDeviceEntry:
    config_entries: set[str]
    connections: set[tuple[str, str]]
    identifiers: set[tuple[str, str]]
    id: str
    orphaned_timestamp: float | None
    created_at: datetime
    modified_at: datetime
    _cache: dict[str, Any]
    def to_device_entry(self, config_entry_id: str, connections: set[tuple[str, str]], identifiers: set[tuple[str, str]]) -> DeviceEntry: ...
    @under_cached_property
    def as_storage_fragment(self) -> json_fragment: ...
    def __init__(self, config_entries, connections, identifiers, id, orphaned_timestamp, created_at, modified_at, cache) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def format_mac(mac: str) -> str: ...

class DeviceRegistryStore(storage.Store[dict[str, list[dict[str, Any]]]]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> dict[str, Any]: ...

class DeviceRegistryItems[_EntryTypeT: (DeviceEntry, DeletedDeviceEntry)](BaseRegistryItems[_EntryTypeT]):
    _connections: dict[tuple[str, str], _EntryTypeT]
    _identifiers: dict[tuple[str, str], _EntryTypeT]
    def __init__(self) -> None: ...
    def _index_entry(self, key: str, entry: _EntryTypeT) -> None: ...
    def _unindex_entry(self, key: str, replacement_entry: _EntryTypeT | None = None) -> None: ...
    def get_entry(self, identifiers: set[tuple[str, str]] | None, connections: set[tuple[str, str]] | None) -> _EntryTypeT | None: ...

class ActiveDeviceRegistryItems(DeviceRegistryItems[DeviceEntry]):
    _area_id_index: RegistryIndexType
    _config_entry_id_index: RegistryIndexType
    _labels_index: RegistryIndexType
    def __init__(self) -> None: ...
    def _index_entry(self, key: str, entry: DeviceEntry) -> None: ...
    def _unindex_entry(self, key: str, replacement_entry: DeviceEntry | None = None) -> None: ...
    def get_devices_for_area_id(self, area_id: str) -> list[DeviceEntry]: ...
    def get_devices_for_label(self, label: str) -> list[DeviceEntry]: ...
    def get_devices_for_config_entry_id(self, config_entry_id: str) -> list[DeviceEntry]: ...

class DeviceRegistry(BaseRegistry[dict[str, list[dict[str, Any]]]]):
    devices: ActiveDeviceRegistryItems
    deleted_devices: DeviceRegistryItems[DeletedDeviceEntry]
    _device_data: dict[str, DeviceEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_get(self, device_id: str) -> DeviceEntry | None: ...
    @callback
    def async_get_device(self, identifiers: set[tuple[str, str]] | None = None, connections: set[tuple[str, str]] | None = None) -> DeviceEntry | None: ...
    def _async_get_deleted_device(self, identifiers: set[tuple[str, str]], connections: set[tuple[str, str]]) -> DeletedDeviceEntry | None: ...
    def _substitute_name_placeholders(self, domain: str, name: str, translation_placeholders: Mapping[str, str]) -> str: ...
    @callback
    def async_get_or_create(self, *, config_entry_id: str, configuration_url: str | URL | None | UndefinedType = ..., connections: set[tuple[str, str]] | None | UndefinedType = ..., created_at: str | datetime | UndefinedType = ..., default_manufacturer: str | None | UndefinedType = ..., default_model: str | None | UndefinedType = ..., default_name: str | None | UndefinedType = ..., disabled_by: DeviceEntryDisabler | None | UndefinedType = ..., entry_type: DeviceEntryType | None | UndefinedType = ..., hw_version: str | None | UndefinedType = ..., identifiers: set[tuple[str, str]] | None | UndefinedType = ..., manufacturer: str | None | UndefinedType = ..., model: str | None | UndefinedType = ..., model_id: str | None | UndefinedType = ..., modified_at: str | datetime | UndefinedType = ..., name: str | None | UndefinedType = ..., serial_number: str | None | UndefinedType = ..., suggested_area: str | None | UndefinedType = ..., sw_version: str | None | UndefinedType = ..., translation_key: str | None = None, translation_placeholders: Mapping[str, str] | None = None, via_device: tuple[str, str] | None | UndefinedType = ...) -> DeviceEntry: ...
    @callback
    def async_update_device(self, device_id: str, *, add_config_entry_id: str | UndefinedType = ..., allow_collisions: bool = False, area_id: str | None | UndefinedType = ..., configuration_url: str | URL | None | UndefinedType = ..., device_info_type: str | UndefinedType = ..., disabled_by: DeviceEntryDisabler | None | UndefinedType = ..., entry_type: DeviceEntryType | None | UndefinedType = ..., hw_version: str | None | UndefinedType = ..., labels: set[str] | UndefinedType = ..., manufacturer: str | None | UndefinedType = ..., merge_connections: set[tuple[str, str]] | UndefinedType = ..., merge_identifiers: set[tuple[str, str]] | UndefinedType = ..., model: str | None | UndefinedType = ..., model_id: str | None | UndefinedType = ..., name_by_user: str | None | UndefinedType = ..., name: str | None | UndefinedType = ..., new_connections: set[tuple[str, str]] | UndefinedType = ..., new_identifiers: set[tuple[str, str]] | UndefinedType = ..., remove_config_entry_id: str | UndefinedType = ..., serial_number: str | None | UndefinedType = ..., suggested_area: str | None | UndefinedType = ..., sw_version: str | None | UndefinedType = ..., via_device_id: str | None | UndefinedType = ...) -> DeviceEntry | None: ...
    @callback
    def _validate_connections(self, device_id: str, connections: set[tuple[str, str]], allow_collisions: bool) -> set[tuple[str, str]]: ...
    @callback
    def _validate_identifiers(self, device_id: str, identifiers: set[tuple[str, str]], allow_collisions: bool) -> set[tuple[str, str]]: ...
    @callback
    def async_remove_device(self, device_id: str) -> None: ...
    async def async_load(self) -> None: ...
    @callback
    def _data_to_save(self) -> dict[str, Any]: ...
    @callback
    def async_clear_config_entry(self, config_entry_id: str) -> None: ...
    @callback
    def async_purge_expired_orphaned_devices(self) -> None: ...
    @callback
    def async_clear_area_id(self, area_id: str) -> None: ...
    @callback
    def async_clear_label_id(self, label_id: str) -> None: ...

@callback
def async_get(hass: HomeAssistant) -> DeviceRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
@callback
def async_entries_for_area(registry: DeviceRegistry, area_id: str) -> list[DeviceEntry]: ...
@callback
def async_entries_for_label(registry: DeviceRegistry, label_id: str) -> list[DeviceEntry]: ...
@callback
def async_entries_for_config_entry(registry: DeviceRegistry, config_entry_id: str) -> list[DeviceEntry]: ...
@callback
def async_config_entry_disabled_by_changed(registry: DeviceRegistry, config_entry: ConfigEntry) -> None: ...
@callback
def async_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry, ent_reg: entity_registry.EntityRegistry) -> None: ...
@callback
def async_setup_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry) -> None: ...
def _normalize_connections(connections: set[tuple[str, str]]) -> set[tuple[str, str]]: ...
