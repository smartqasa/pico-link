from .config import StoredBackupConfig as StoredBackupConfig
from .const import DOMAIN as DOMAIN
from .manager import BackupManager as BackupManager, StoredKnownBackup as StoredKnownBackup
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import TypedDict

STORE_DELAY_SAVE: int
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int

class StoredBackupData(TypedDict):
    backups: list[StoredKnownBackup]
    config: StoredBackupConfig

class BackupStore:
    _hass: Incomplete
    _manager: Incomplete
    _store: Store[StoredBackupData]
    def __init__(self, hass: HomeAssistant, manager: BackupManager) -> None: ...
    async def load(self) -> StoredBackupData | None: ...
    @callback
    def save(self) -> None: ...
    @callback
    def _data_to_save(self) -> StoredBackupData: ...
