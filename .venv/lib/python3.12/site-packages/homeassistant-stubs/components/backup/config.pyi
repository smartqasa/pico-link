from .const import LOGGER as LOGGER
from .manager import BackupManager as BackupManager, ManagerBackup as ManagerBackup
from .models import BackupManagerError as BackupManagerError, Folder as Folder
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from cronsim import CronSim
from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_point_in_time as async_track_point_in_time
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Self, TypedDict

CRON_PATTERN_DAILY: str
CRON_PATTERN_WEEKLY: str
BACKUP_START_TIME_JITTER: Incomplete

class StoredBackupConfig(TypedDict):
    create_backup: StoredCreateBackupConfig
    last_attempted_automatic_backup: str | None
    last_completed_automatic_backup: str | None
    retention: StoredRetentionConfig
    schedule: StoredBackupSchedule

@dataclass(kw_only=True)
class BackupConfigData:
    create_backup: CreateBackupConfig
    last_attempted_automatic_backup: datetime | None = ...
    last_completed_automatic_backup: datetime | None = ...
    retention: RetentionConfig
    schedule: BackupSchedule
    @classmethod
    def from_dict(cls, data: StoredBackupConfig) -> Self: ...
    def to_dict(self) -> StoredBackupConfig: ...

class BackupConfig:
    data: Incomplete
    _manager: Incomplete
    def __init__(self, hass: HomeAssistant, manager: BackupManager) -> None: ...
    def load(self, stored_config: StoredBackupConfig) -> None: ...
    async def update(self, *, create_backup: CreateBackupParametersDict | UndefinedType = ..., retention: RetentionParametersDict | UndefinedType = ..., schedule: ScheduleState | UndefinedType = ...) -> None: ...

@dataclass(kw_only=True)
class RetentionConfig:
    copies: int | None = ...
    days: int | None = ...
    def apply(self, manager: BackupManager) -> None: ...
    def to_dict(self) -> StoredRetentionConfig: ...
    @callback
    def _schedule_next(self, manager: BackupManager) -> None: ...
    @callback
    def _unschedule_next(self, manager: BackupManager) -> None: ...

class StoredRetentionConfig(TypedDict):
    copies: int | None
    days: int | None

class RetentionParametersDict(TypedDict, total=False):
    copies: int | None
    days: int | None

class StoredBackupSchedule(TypedDict):
    state: ScheduleState

class ScheduleState(StrEnum):
    NEVER = 'never'
    DAILY = 'daily'
    MONDAY = 'mon'
    TUESDAY = 'tue'
    WEDNESDAY = 'wed'
    THURSDAY = 'thu'
    FRIDAY = 'fri'
    SATURDAY = 'sat'
    SUNDAY = 'sun'

@dataclass(kw_only=True)
class BackupSchedule:
    state: ScheduleState = ...
    cron_event: CronSim | None = field(init=False, default=None)
    @callback
    def apply(self, manager: BackupManager) -> None: ...
    @callback
    def _schedule_next(self, cron_pattern: str, manager: BackupManager) -> None: ...
    def to_dict(self) -> StoredBackupSchedule: ...
    @callback
    def _unschedule_next(self, manager: BackupManager) -> None: ...

@dataclass(kw_only=True)
class CreateBackupConfig:
    agent_ids: list[str] = field(default_factory=list)
    include_addons: list[str] | None = ...
    include_all_addons: bool = ...
    include_database: bool = ...
    include_folders: list[Folder] | None = ...
    name: str | None = ...
    password: str | None = ...
    def to_dict(self) -> StoredCreateBackupConfig: ...

class StoredCreateBackupConfig(TypedDict):
    agent_ids: list[str]
    include_addons: list[str] | None
    include_all_addons: bool
    include_database: bool
    include_folders: list[Folder] | None
    name: str | None
    password: str | None

class CreateBackupParametersDict(TypedDict, total=False):
    agent_ids: list[str]
    include_addons: list[str] | None
    include_all_addons: bool
    include_database: bool
    include_folders: list[Folder] | None
    name: str | None
    password: str | None

async def _delete_filtered_backups(manager: BackupManager, backup_filter: Callable[[dict[str, ManagerBackup]], dict[str, ManagerBackup]]) -> None: ...
async def delete_backups_exceeding_configured_count(manager: BackupManager) -> None: ...
