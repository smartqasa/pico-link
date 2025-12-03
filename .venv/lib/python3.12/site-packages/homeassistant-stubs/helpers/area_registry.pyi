from .json import json_bytes as json_bytes, json_fragment as json_fragment
from .normalized_name_base_registry import NormalizedNameBaseRegistryEntry as NormalizedNameBaseRegistryEntry, NormalizedNameBaseRegistryItems as NormalizedNameBaseRegistryItems
from .registry import BaseRegistry as BaseRegistry, RegistryIndexType as RegistryIndexType
from .singleton import singleton as singleton
from .storage import Store as Store
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass, field
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp, utcnow as utcnow
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property as under_cached_property
from typing import Any, Literal, TypedDict

DATA_REGISTRY: HassKey[AreaRegistry]
EVENT_AREA_REGISTRY_UPDATED: EventType[EventAreaRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int

class _AreaStoreData(TypedDict):
    aliases: list[str]
    floor_id: str | None
    icon: str | None
    id: str
    labels: list[str]
    name: str
    picture: str | None
    created_at: str
    modified_at: str

class AreasRegistryStoreData(TypedDict):
    areas: list[_AreaStoreData]

class EventAreaRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    area_id: str

@dataclass(frozen=True, kw_only=True, slots=True)
class AreaEntry(NormalizedNameBaseRegistryEntry):
    aliases: set[str]
    floor_id: str | None
    icon: str | None
    id: str
    labels: set[str] = field(default_factory=set)
    picture: str | None
    _cache: dict[str, Any] = field(default_factory=dict, compare=False, init=False)
    @under_cached_property
    def json_fragment(self) -> json_fragment: ...

class AreaRegistryStore(Store[AreasRegistryStoreData]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> AreasRegistryStoreData: ...

class AreaRegistryItems(NormalizedNameBaseRegistryItems[AreaEntry]):
    _labels_index: RegistryIndexType
    _floors_index: RegistryIndexType
    def __init__(self) -> None: ...
    def _index_entry(self, key: str, entry: AreaEntry) -> None: ...
    def _unindex_entry(self, key: str, replacement_entry: AreaEntry | None = None) -> None: ...
    def get_areas_for_label(self, label: str) -> list[AreaEntry]: ...
    def get_areas_for_floor(self, floor: str) -> list[AreaEntry]: ...

class AreaRegistry(BaseRegistry[AreasRegistryStoreData]):
    areas: AreaRegistryItems
    _area_data: dict[str, AreaEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_get_area(self, area_id: str) -> AreaEntry | None: ...
    @callback
    def async_get_area_by_name(self, name: str) -> AreaEntry | None: ...
    @callback
    def async_list_areas(self) -> Iterable[AreaEntry]: ...
    @callback
    def async_get_or_create(self, name: str) -> AreaEntry: ...
    def _generate_id(self, name: str) -> str: ...
    @callback
    def async_create(self, name: str, *, aliases: set[str] | None = None, floor_id: str | None = None, icon: str | None = None, labels: set[str] | None = None, picture: str | None = None) -> AreaEntry: ...
    @callback
    def async_delete(self, area_id: str) -> None: ...
    @callback
    def async_update(self, area_id: str, *, aliases: set[str] | UndefinedType = ..., floor_id: str | None | UndefinedType = ..., icon: str | None | UndefinedType = ..., labels: set[str] | UndefinedType = ..., name: str | UndefinedType = ..., picture: str | None | UndefinedType = ...) -> AreaEntry: ...
    @callback
    def _async_update(self, area_id: str, *, aliases: set[str] | UndefinedType = ..., floor_id: str | None | UndefinedType = ..., icon: str | None | UndefinedType = ..., labels: set[str] | UndefinedType = ..., name: str | UndefinedType = ..., picture: str | None | UndefinedType = ...) -> AreaEntry: ...
    async def async_load(self) -> None: ...
    @callback
    def _data_to_save(self) -> AreasRegistryStoreData: ...
    @callback
    def _async_setup_cleanup(self) -> None: ...

@callback
def async_get(hass: HomeAssistant) -> AreaRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
@callback
def async_entries_for_floor(registry: AreaRegistry, floor_id: str) -> list[AreaEntry]: ...
@callback
def async_entries_for_label(registry: AreaRegistry, label_id: str) -> list[AreaEntry]: ...
