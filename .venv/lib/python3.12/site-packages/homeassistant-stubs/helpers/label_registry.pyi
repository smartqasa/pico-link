from .normalized_name_base_registry import NormalizedNameBaseRegistryEntry as NormalizedNameBaseRegistryEntry, NormalizedNameBaseRegistryItems as NormalizedNameBaseRegistryItems
from .registry import BaseRegistry as BaseRegistry
from .singleton import singleton as singleton
from .storage import Store as Store
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp, utcnow as utcnow
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Literal, TypedDict

DATA_REGISTRY: HassKey[LabelRegistry]
EVENT_LABEL_REGISTRY_UPDATED: EventType[EventLabelRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int

class _LabelStoreData(TypedDict):
    color: str | None
    description: str | None
    icon: str | None
    label_id: str
    name: str
    created_at: str
    modified_at: str

class LabelRegistryStoreData(TypedDict):
    labels: list[_LabelStoreData]

class EventLabelRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    label_id: str
type EventLabelRegistryUpdated = Event[EventLabelRegistryUpdatedData]

@dataclass(slots=True, frozen=True, kw_only=True)
class LabelEntry(NormalizedNameBaseRegistryEntry):
    label_id: str
    description: str | None = ...
    color: str | None = ...
    icon: str | None = ...

class LabelRegistryStore(Store[LabelRegistryStoreData]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> LabelRegistryStoreData: ...

class LabelRegistry(BaseRegistry[LabelRegistryStoreData]):
    labels: NormalizedNameBaseRegistryItems[LabelEntry]
    _label_data: dict[str, LabelEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_get_label(self, label_id: str) -> LabelEntry | None: ...
    @callback
    def async_get_label_by_name(self, name: str) -> LabelEntry | None: ...
    @callback
    def async_list_labels(self) -> Iterable[LabelEntry]: ...
    def _generate_id(self, name: str) -> str: ...
    @callback
    def async_create(self, name: str, *, color: str | None = None, icon: str | None = None, description: str | None = None) -> LabelEntry: ...
    @callback
    def async_delete(self, label_id: str) -> None: ...
    @callback
    def async_update(self, label_id: str, *, color: str | None | UndefinedType = ..., description: str | None | UndefinedType = ..., icon: str | None | UndefinedType = ..., name: str | UndefinedType = ...) -> LabelEntry: ...
    async def async_load(self) -> None: ...
    @callback
    def _data_to_save(self) -> LabelRegistryStoreData: ...

@callback
def async_get(hass: HomeAssistant) -> LabelRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
