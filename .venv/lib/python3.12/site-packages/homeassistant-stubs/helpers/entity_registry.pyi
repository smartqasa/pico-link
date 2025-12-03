from . import storage as storage
from .device_registry import EVENT_DEVICE_REGISTRY_UPDATED as EVENT_DEVICE_REGISTRY_UPDATED, EventDeviceRegistryUpdatedData as EventDeviceRegistryUpdatedData
from .json import JSON_DUMP as JSON_DUMP, find_paths_unserializable_data as find_paths_unserializable_data, json_bytes as json_bytes, json_fragment as json_fragment
from .registry import BaseRegistry as BaseRegistry, BaseRegistryItems as BaseRegistryItems, RegistryIndexType as RegistryIndexType
from .singleton import singleton as singleton
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Container, Hashable, KeysView, Mapping
from datetime import datetime
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, ATTR_RESTORED as ATTR_RESTORED, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EntityCategory as EntityCategory, MAX_LENGTH_STATE_DOMAIN as MAX_LENGTH_STATE_DOMAIN, MAX_LENGTH_STATE_ENTITY_ID as MAX_LENGTH_STATE_ENTITY_ID, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.exceptions import MaxLengthExceeded as MaxLengthExceeded
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from homeassistant.util import slugify as slugify
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp, utcnow as utcnow
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.json import format_unserializable_data as format_unserializable_data
from homeassistant.util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from propcache import cached_property as under_cached_property
from typing import Any, Literal, NotRequired, TypedDict

DATA_REGISTRY: HassKey[EntityRegistry]
EVENT_ENTITY_REGISTRY_UPDATED: EventType[EventEntityRegistryUpdatedData]
_LOGGER: Incomplete
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int
STORAGE_KEY: str
CLEANUP_INTERVAL: Incomplete
ORPHANED_ENTITY_KEEP_SECONDS: Incomplete
ENTITY_CATEGORY_VALUE_TO_INDEX: dict[EntityCategory | None, int]
ENTITY_CATEGORY_INDEX_TO_VALUE: Incomplete
ENTITY_DESCRIBING_ATTRIBUTES: Incomplete

class RegistryEntryDisabler(StrEnum):
    CONFIG_ENTRY = 'config_entry'
    DEVICE = 'device'
    HASS = 'hass'
    INTEGRATION = 'integration'
    USER = 'user'

class RegistryEntryHider(StrEnum):
    INTEGRATION = 'integration'
    USER = 'user'

class _EventEntityRegistryUpdatedData_CreateRemove(TypedDict):
    action: Literal['create', 'remove']
    entity_id: str

class _EventEntityRegistryUpdatedData_Update(TypedDict):
    action: Literal['update']
    entity_id: str
    changes: dict[str, Any]
    old_entity_id: NotRequired[str]
type EventEntityRegistryUpdatedData = _EventEntityRegistryUpdatedData_CreateRemove | _EventEntityRegistryUpdatedData_Update
type EntityOptionsType = Mapping[str, Mapping[str, Any]]
type ReadOnlyEntityOptionsType = ReadOnlyDict[str, ReadOnlyDict[str, Any]]

DISPLAY_DICT_OPTIONAL: Incomplete

def _protect_entity_options(data: EntityOptionsType | None) -> ReadOnlyEntityOptionsType: ...

class RegistryEntry:
    entity_id: str
    unique_id: str
    platform: str
    previous_unique_id: str | None
    aliases: set[str]
    area_id: str | None
    categories: dict[str, str]
    capabilities: Mapping[str, Any] | None
    config_entry_id: str | None
    created_at: datetime
    device_class: str | None
    device_id: str | None
    domain: str
    disabled_by: RegistryEntryDisabler | None
    entity_category: EntityCategory | None
    hidden_by: RegistryEntryHider | None
    icon: str | None
    id: str
    has_entity_name: bool
    labels: set[str]
    modified_at: datetime
    name: str | None
    options: ReadOnlyEntityOptionsType
    original_device_class: str | None
    original_icon: str | None
    original_name: str | None
    supported_features: int
    translation_key: str | None
    unit_of_measurement: str | None
    _cache: dict[str, Any]
    @domain.default
    def _domain_default(self) -> str: ...
    @property
    def disabled(self) -> bool: ...
    @property
    def hidden(self) -> bool: ...
    @property
    def _as_display_dict(self) -> dict[str, Any] | None: ...
    @under_cached_property
    def display_json_repr(self) -> bytes | None: ...
    @under_cached_property
    def as_partial_dict(self) -> dict[str, Any]: ...
    @under_cached_property
    def extended_dict(self) -> dict[str, Any]: ...
    @under_cached_property
    def partial_json_repr(self) -> bytes | None: ...
    @under_cached_property
    def as_storage_fragment(self) -> json_fragment: ...
    @callback
    def write_unavailable_state(self, hass: HomeAssistant) -> None: ...
    def __init__(self, entity_id, unique_id, platform, previous_unique_id, aliases, area_id, categories, capabilities, config_entry_id, created_at, device_class, device_id, domain, disabled_by, entity_category, hidden_by, icon, id, has_entity_name, labels, modified_at, name, options, original_device_class, original_icon, original_name, supported_features, translation_key, unit_of_measurement, cache) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class DeletedRegistryEntry:
    entity_id: str
    unique_id: str
    platform: str
    config_entry_id: str | None
    domain: str
    id: str
    orphaned_timestamp: float | None
    created_at: datetime
    modified_at: datetime
    _cache: dict[str, Any]
    @domain.default
    def _domain_default(self) -> str: ...
    @under_cached_property
    def as_storage_fragment(self) -> json_fragment: ...
    def __init__(self, entity_id, unique_id, platform, config_entry_id, domain, id, orphaned_timestamp, created_at, modified_at, cache) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class EntityRegistryStore(storage.Store[dict[str, list[dict[str, Any]]]]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> dict: ...

class EntityRegistryItems(BaseRegistryItems[RegistryEntry]):
    _entry_ids: dict[str, RegistryEntry]
    _index: dict[tuple[str, str, str], str]
    _config_entry_id_index: RegistryIndexType
    _device_id_index: RegistryIndexType
    _area_id_index: RegistryIndexType
    _labels_index: RegistryIndexType
    def __init__(self) -> None: ...
    def _index_entry(self, key: str, entry: RegistryEntry) -> None: ...
    def _unindex_entry(self, key: str, replacement_entry: RegistryEntry | None = None) -> None: ...
    def get_device_ids(self) -> KeysView[str]: ...
    def get_entity_id(self, key: tuple[str, str, str]) -> str | None: ...
    def get_entry(self, key: str) -> RegistryEntry | None: ...
    def get_entries_for_device_id(self, device_id: str, include_disabled_entities: bool = False) -> list[RegistryEntry]: ...
    def get_entries_for_config_entry_id(self, config_entry_id: str) -> list[RegistryEntry]: ...
    def get_entries_for_area_id(self, area_id: str) -> list[RegistryEntry]: ...
    def get_entries_for_label(self, label: str) -> list[RegistryEntry]: ...

def _validate_item(hass: HomeAssistant, domain: str, platform: str, *, disabled_by: RegistryEntryDisabler | None | UndefinedType = None, entity_category: EntityCategory | None | UndefinedType = None, hidden_by: RegistryEntryHider | None | UndefinedType = None, report_non_string_unique_id: bool = True, unique_id: str | Hashable | UndefinedType | Any) -> None: ...

class EntityRegistry(BaseRegistry):
    deleted_entities: dict[tuple[str, str, str], DeletedRegistryEntry]
    entities: EntityRegistryItems
    _entities_data: dict[str, RegistryEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_is_registered(self, entity_id: str) -> bool: ...
    @callback
    def async_get(self, entity_id_or_uuid: str) -> RegistryEntry | None: ...
    @callback
    def async_get_entity_id(self, domain: str, platform: str, unique_id: str) -> str | None: ...
    @callback
    def async_device_ids(self) -> list[str]: ...
    def _entity_id_available(self, entity_id: str, known_object_ids: Container[str] | None) -> bool: ...
    @callback
    def async_generate_entity_id(self, domain: str, suggested_object_id: str, known_object_ids: Container[str] | None = None) -> str: ...
    @callback
    def async_get_or_create(self, domain: str, platform: str, unique_id: str, *, known_object_ids: Container[str] | None = None, suggested_object_id: str | None = None, disabled_by: RegistryEntryDisabler | None = None, hidden_by: RegistryEntryHider | None = None, get_initial_options: Callable[[], EntityOptionsType | None] | None = None, capabilities: Mapping[str, Any] | None | UndefinedType = ..., config_entry: ConfigEntry | None | UndefinedType = ..., device_id: str | None | UndefinedType = ..., entity_category: EntityCategory | UndefinedType | None = ..., has_entity_name: bool | UndefinedType = ..., original_device_class: str | None | UndefinedType = ..., original_icon: str | None | UndefinedType = ..., original_name: str | None | UndefinedType = ..., supported_features: int | None | UndefinedType = ..., translation_key: str | None | UndefinedType = ..., unit_of_measurement: str | None | UndefinedType = ...) -> RegistryEntry: ...
    @callback
    def async_remove(self, entity_id: str) -> None: ...
    @callback
    def async_device_modified(self, event: Event[EventDeviceRegistryUpdatedData]) -> None: ...
    @callback
    def _async_update_entity(self, entity_id: str, *, aliases: set[str] | UndefinedType = ..., area_id: str | None | UndefinedType = ..., categories: dict[str, str] | UndefinedType = ..., capabilities: Mapping[str, Any] | None | UndefinedType = ..., config_entry_id: str | None | UndefinedType = ..., device_class: str | None | UndefinedType = ..., device_id: str | None | UndefinedType = ..., disabled_by: RegistryEntryDisabler | None | UndefinedType = ..., entity_category: EntityCategory | None | UndefinedType = ..., hidden_by: RegistryEntryHider | None | UndefinedType = ..., icon: str | None | UndefinedType = ..., has_entity_name: bool | UndefinedType = ..., labels: set[str] | UndefinedType = ..., name: str | None | UndefinedType = ..., new_entity_id: str | UndefinedType = ..., new_unique_id: str | UndefinedType = ..., options: EntityOptionsType | UndefinedType = ..., original_device_class: str | None | UndefinedType = ..., original_icon: str | None | UndefinedType = ..., original_name: str | None | UndefinedType = ..., platform: str | None | UndefinedType = ..., supported_features: int | UndefinedType = ..., translation_key: str | None | UndefinedType = ..., unit_of_measurement: str | None | UndefinedType = ...) -> RegistryEntry: ...
    @callback
    def async_update_entity(self, entity_id: str, *, aliases: set[str] | UndefinedType = ..., area_id: str | None | UndefinedType = ..., categories: dict[str, str] | UndefinedType = ..., capabilities: Mapping[str, Any] | None | UndefinedType = ..., config_entry_id: str | None | UndefinedType = ..., device_class: str | None | UndefinedType = ..., device_id: str | None | UndefinedType = ..., disabled_by: RegistryEntryDisabler | None | UndefinedType = ..., entity_category: EntityCategory | None | UndefinedType = ..., hidden_by: RegistryEntryHider | None | UndefinedType = ..., icon: str | None | UndefinedType = ..., has_entity_name: bool | UndefinedType = ..., labels: set[str] | UndefinedType = ..., name: str | None | UndefinedType = ..., new_entity_id: str | UndefinedType = ..., new_unique_id: str | UndefinedType = ..., original_device_class: str | None | UndefinedType = ..., original_icon: str | None | UndefinedType = ..., original_name: str | None | UndefinedType = ..., supported_features: int | UndefinedType = ..., translation_key: str | None | UndefinedType = ..., unit_of_measurement: str | None | UndefinedType = ...) -> RegistryEntry: ...
    @callback
    def async_update_entity_platform(self, entity_id: str, new_platform: str, *, new_config_entry_id: str | UndefinedType = ..., new_unique_id: str | UndefinedType = ..., new_device_id: str | None | UndefinedType = ...) -> RegistryEntry: ...
    @callback
    def async_update_entity_options(self, entity_id: str, domain: str, options: Mapping[str, Any] | None) -> RegistryEntry: ...
    async def async_load(self) -> None: ...
    @callback
    def _data_to_save(self) -> dict[str, Any]: ...
    @callback
    def async_clear_category_id(self, scope: str, category_id: str) -> None: ...
    @callback
    def async_clear_label_id(self, label_id: str) -> None: ...
    @callback
    def async_clear_config_entry(self, config_entry_id: str) -> None: ...
    @callback
    def async_purge_expired_orphaned_entities(self) -> None: ...
    @callback
    def async_clear_area_id(self, area_id: str) -> None: ...

@callback
def async_get(hass: HomeAssistant) -> EntityRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
@callback
def async_entries_for_device(registry: EntityRegistry, device_id: str, include_disabled_entities: bool = False) -> list[RegistryEntry]: ...
@callback
def async_entries_for_area(registry: EntityRegistry, area_id: str) -> list[RegistryEntry]: ...
@callback
def async_entries_for_label(registry: EntityRegistry, label_id: str) -> list[RegistryEntry]: ...
@callback
def async_entries_for_category(registry: EntityRegistry, scope: str, category_id: str) -> list[RegistryEntry]: ...
@callback
def async_entries_for_config_entry(registry: EntityRegistry, config_entry_id: str) -> list[RegistryEntry]: ...
@callback
def async_config_entry_disabled_by_changed(registry: EntityRegistry, config_entry: ConfigEntry) -> None: ...
@callback
def _async_setup_cleanup(hass: HomeAssistant, registry: EntityRegistry) -> None: ...
@callback
def _async_setup_entity_restore(hass: HomeAssistant, registry: EntityRegistry) -> None: ...
async def async_migrate_entries(hass: HomeAssistant, config_entry_id: str, entry_callback: Callable[[RegistryEntry], dict[str, Any] | None]) -> None: ...
@callback
def async_validate_entity_id(registry: EntityRegistry, entity_id_or_uuid: str) -> str: ...
@callback
def async_resolve_entity_id(registry: EntityRegistry, entity_id_or_uuid: str) -> str | None: ...
@callback
def async_validate_entity_ids(registry: EntityRegistry, entity_ids_or_uuids: list[str]) -> list[str]: ...
