from .util import get_iid_storage_filename_for_entry_id as get_iid_storage_filename_for_entry_id
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from uuid import UUID

IID_MANAGER_STORAGE_VERSION: int
IID_MANAGER_SAVE_DELAY: int
ALLOCATIONS_KEY: str
IID_MIN: int
IID_MAX: int
ACCESSORY_INFORMATION_SERVICE: str

class IIDStorage(Store):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict) -> dict: ...

class AccessoryIIDStorage:
    hass: Incomplete
    allocations: dict[str, dict[str, int]]
    allocated_iids: dict[str, list[int]]
    entry_id: Incomplete
    store: IIDStorage | None
    def __init__(self, hass: HomeAssistant, entry_id: str) -> None: ...
    async def async_initialize(self) -> None: ...
    def get_or_allocate_iid(self, aid: int, service_uuid: UUID, service_unique_id: str | None, char_uuid: UUID | None, char_unique_id: str | None) -> int: ...
    @callback
    def _async_schedule_save(self) -> None: ...
    async def async_save(self) -> None: ...
    @callback
    def _data_to_save(self) -> dict[str, dict[str, dict[str, int]]]: ...
