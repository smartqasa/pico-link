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

DATA_REGISTRY: HassKey[FloorRegistry]
EVENT_FLOOR_REGISTRY_UPDATED: EventType[EventFloorRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int

class _FloorStoreData(TypedDict):
    aliases: list[str]
    floor_id: str
    icon: str | None
    level: int | None
    name: str
    created_at: str
    modified_at: str

class FloorRegistryStoreData(TypedDict):
    floors: list[_FloorStoreData]

class EventFloorRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    floor_id: str
type EventFloorRegistryUpdated = Event[EventFloorRegistryUpdatedData]

@dataclass(slots=True, kw_only=True, frozen=True)
class FloorEntry(NormalizedNameBaseRegistryEntry):
    aliases: set[str]
    floor_id: str
    icon: str | None = ...
    level: int | None = ...

class FloorRegistryStore(Store[FloorRegistryStoreData]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> FloorRegistryStoreData: ...

class FloorRegistry(BaseRegistry[FloorRegistryStoreData]):
    floors: NormalizedNameBaseRegistryItems[FloorEntry]
    _floor_data: dict[str, FloorEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_get_floor(self, floor_id: str) -> FloorEntry | None: ...
    @callback
    def async_get_floor_by_name(self, name: str) -> FloorEntry | None: ...
    @callback
    def async_list_floors(self) -> Iterable[FloorEntry]: ...
    def _generate_id(self, name: str) -> str: ...
    @callback
    def async_create(self, name: str, *, aliases: set[str] | None = None, icon: str | None = None, level: int | None = None) -> FloorEntry: ...
    @callback
    def async_delete(self, floor_id: str) -> None: ...
    @callback
    def async_update(self, floor_id: str, *, aliases: set[str] | UndefinedType = ..., icon: str | None | UndefinedType = ..., level: int | UndefinedType = ..., name: str | UndefinedType = ...) -> FloorEntry: ...
    async def async_load(self) -> None: ...
    @callback
    def _data_to_save(self) -> FloorRegistryStoreData: ...

@callback
def async_get(hass: HomeAssistant) -> FloorRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
