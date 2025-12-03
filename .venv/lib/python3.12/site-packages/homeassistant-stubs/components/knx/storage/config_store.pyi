import abc
from ..const import DOMAIN as DOMAIN
from .const import CONF_DATA as CONF_DATA
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.ulid import ulid_now as ulid_now
from typing import Any, Final, TypedDict

_LOGGER: Incomplete
STORAGE_VERSION: Final[int]
STORAGE_KEY: Final[Incomplete]
type KNXPlatformStoreModel = dict[str, dict[str, Any]]
type KNXEntityStoreModel = dict[str, KNXPlatformStoreModel]

class KNXConfigStoreModel(TypedDict):
    entities: KNXEntityStoreModel

class PlatformControllerBase(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    async def create_entity(self, unique_id: str, config: dict[str, Any]) -> None: ...
    @abstractmethod
    async def update_entity(self, entity_entry: er.RegistryEntry, config: dict[str, Any]) -> None: ...

class KNXConfigStore:
    hass: Incomplete
    config_entry: Incomplete
    _store: Incomplete
    data: Incomplete
    _platform_controllers: dict[Platform, PlatformControllerBase]
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def load_data(self) -> None: ...
    def add_platform(self, platform: Platform, controller: PlatformControllerBase) -> None: ...
    async def create_entity(self, platform: Platform, data: dict[str, Any]) -> str | None: ...
    @callback
    def get_entity_config(self, entity_id: str) -> dict[str, Any]: ...
    async def update_entity(self, platform: Platform, entity_id: str, data: dict[str, Any]) -> None: ...
    async def delete_entity(self, entity_id: str) -> None: ...
    def get_entity_entries(self) -> list[er.RegistryEntry]: ...

class ConfigStoreException(Exception): ...
