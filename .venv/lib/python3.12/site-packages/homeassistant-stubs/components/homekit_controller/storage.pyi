from .const import DOMAIN as DOMAIN, ENTITY_MAP as ENTITY_MAP
from _typeshed import Incomplete
from aiohomekit.characteristic_cache import Pairing, StorageLayout
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import Any

ENTITY_MAP_STORAGE_KEY: Incomplete
ENTITY_MAP_STORAGE_VERSION: int
ENTITY_MAP_SAVE_DELAY: int
_LOGGER: Incomplete

class EntityMapStorage:
    hass: Incomplete
    store: Incomplete
    storage_data: dict[str, Pairing]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    def get_map(self, homekit_id: str) -> Pairing | None: ...
    @callback
    def async_create_or_update_map(self, homekit_id: str, config_num: int, accessories: list[Any], broadcast_key: str | None = None, state_num: int | None = None) -> Pairing: ...
    @callback
    def async_delete_map(self, homekit_id: str) -> None: ...
    @callback
    def _async_schedule_save(self) -> None: ...
    @callback
    def _data_to_save(self) -> StorageLayout: ...

async def async_get_entity_storage(hass: HomeAssistant) -> EntityMapStorage: ...
