import abc
import aiohttp
import asyncio
from .agent import BackupAgent as BackupAgent, BackupAgentError as BackupAgentError, BackupAgentPlatformProtocol as BackupAgentPlatformProtocol, LocalBackupAgent as LocalBackupAgent
from .config import BackupConfig as BackupConfig, delete_backups_exceeding_configured_count as delete_backups_exceeding_configured_count
from .const import BUF_SIZE as BUF_SIZE, DATA_MANAGER as DATA_MANAGER, DOMAIN as DOMAIN, EXCLUDE_DATABASE_FROM_BACKUP as EXCLUDE_DATABASE_FROM_BACKUP, EXCLUDE_FROM_BACKUP as EXCLUDE_FROM_BACKUP, LOGGER as LOGGER
from .models import AgentBackup as AgentBackup, BackupManagerError as BackupManagerError, Folder as Folder
from .store import BackupStore as BackupStore
from .util import make_backup_dir as make_backup_dir, read_backup as read_backup, validate_password as validate_password
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.backup_restore import RESTORE_BACKUP_FILE as RESTORE_BACKUP_FILE, password_to_key as password_to_key
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import instance_id as instance_id, integration_platform as integration_platform
from homeassistant.helpers.json import json_bytes as json_bytes
from pathlib import Path
from typing import Any, Protocol, TypedDict

@dataclass(frozen=True, kw_only=True, slots=True)
class NewBackup:
    backup_job_id: str

@dataclass(frozen=True, kw_only=True, slots=True)
class ManagerBackup(AgentBackup):
    agent_ids: list[str]
    failed_agent_ids: list[str]
    with_automatic_settings: bool | None

@dataclass(frozen=True, kw_only=True, slots=True)
class WrittenBackup:
    backup: AgentBackup
    open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]]
    release_stream: Callable[[], Coroutine[Any, Any, None]]

class BackupManagerState(StrEnum):
    IDLE = 'idle'
    CREATE_BACKUP = 'create_backup'
    RECEIVE_BACKUP = 'receive_backup'
    RESTORE_BACKUP = 'restore_backup'

class CreateBackupStage(StrEnum):
    ADDON_REPOSITORIES = 'addon_repositories'
    ADDONS = 'addons'
    AWAIT_ADDON_RESTARTS = 'await_addon_restarts'
    DOCKER_CONFIG = 'docker_config'
    FINISHING_FILE = 'finishing_file'
    FOLDERS = 'folders'
    HOME_ASSISTANT = 'home_assistant'
    UPLOAD_TO_AGENTS = 'upload_to_agents'

class CreateBackupState(StrEnum):
    COMPLETED = 'completed'
    FAILED = 'failed'
    IN_PROGRESS = 'in_progress'

class ReceiveBackupStage(StrEnum):
    RECEIVE_FILE = 'receive_file'
    UPLOAD_TO_AGENTS = 'upload_to_agents'

class ReceiveBackupState(StrEnum):
    COMPLETED = 'completed'
    FAILED = 'failed'
    IN_PROGRESS = 'in_progress'

class RestoreBackupStage(StrEnum):
    ADDON_REPOSITORIES = 'addon_repositories'
    ADDONS = 'addons'
    AWAIT_ADDON_RESTARTS = 'await_addon_restarts'
    AWAIT_HOME_ASSISTANT_RESTART = 'await_home_assistant_restart'
    CHECK_HOME_ASSISTANT = 'check_home_assistant'
    DOCKER_CONFIG = 'docker_config'
    DOWNLOAD_FROM_AGENT = 'download_from_agent'
    FOLDERS = 'folders'
    HOME_ASSISTANT = 'home_assistant'
    REMOVE_DELTA_ADDONS = 'remove_delta_addons'

class RestoreBackupState(StrEnum):
    COMPLETED = 'completed'
    FAILED = 'failed'
    IN_PROGRESS = 'in_progress'

@dataclass(frozen=True, kw_only=True, slots=True)
class ManagerStateEvent:
    manager_state: BackupManagerState

@dataclass(frozen=True, kw_only=True, slots=True)
class IdleEvent(ManagerStateEvent):
    manager_state: BackupManagerState = ...

@dataclass(frozen=True, kw_only=True, slots=True)
class CreateBackupEvent(ManagerStateEvent):
    manager_state: BackupManagerState = ...
    stage: CreateBackupStage | None
    state: CreateBackupState

@dataclass(frozen=True, kw_only=True, slots=True)
class ReceiveBackupEvent(ManagerStateEvent):
    manager_state: BackupManagerState = ...
    stage: ReceiveBackupStage | None
    state: ReceiveBackupState

@dataclass(frozen=True, kw_only=True, slots=True)
class RestoreBackupEvent(ManagerStateEvent):
    manager_state: BackupManagerState = ...
    stage: RestoreBackupStage | None
    state: RestoreBackupState

class BackupPlatformProtocol(Protocol):
    async def async_pre_backup(self, hass: HomeAssistant) -> None: ...
    async def async_post_backup(self, hass: HomeAssistant) -> None: ...

class BackupReaderWriter(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def async_create_backup(self, *, agent_ids: list[str], backup_name: str, extra_metadata: dict[str, bool | str], include_addons: list[str] | None, include_all_addons: bool, include_database: bool, include_folders: list[Folder] | None, include_homeassistant: bool, on_progress: Callable[[ManagerStateEvent], None], password: str | None) -> tuple[NewBackup, asyncio.Task[WrittenBackup]]: ...
    @abc.abstractmethod
    async def async_receive_backup(self, *, agent_ids: list[str], stream: AsyncIterator[bytes], suggested_filename: str) -> WrittenBackup: ...
    @abc.abstractmethod
    async def async_restore_backup(self, backup_id: str, *, agent_id: str, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], password: str | None, restore_addons: list[str] | None, restore_database: bool, restore_folders: list[Folder] | None, restore_homeassistant: bool) -> None: ...

class BackupReaderWriterError(HomeAssistantError): ...
class IncorrectPasswordError(BackupReaderWriterError): ...

class BackupManager:
    hass: Incomplete
    platforms: dict[str, BackupPlatformProtocol]
    backup_agent_platforms: dict[str, BackupAgentPlatformProtocol]
    backup_agents: dict[str, BackupAgent]
    local_backup_agents: dict[str, LocalBackupAgent]
    config: Incomplete
    _reader_writer: Incomplete
    known_backups: Incomplete
    store: Incomplete
    _backup_task: asyncio.Task[WrittenBackup] | None
    _backup_finish_task: asyncio.Task[None] | None
    remove_next_backup_event: Callable[[], None] | None
    remove_next_delete_event: Callable[[], None] | None
    last_event: ManagerStateEvent
    _backup_event_subscriptions: list[Callable[[ManagerStateEvent], None]]
    def __init__(self, hass: HomeAssistant, reader_writer: BackupReaderWriter) -> None: ...
    async def async_setup(self) -> None: ...
    @property
    def state(self) -> BackupManagerState: ...
    @callback
    def _add_platform_pre_post_handler(self, integration_domain: str, platform: BackupPlatformProtocol) -> None: ...
    @callback
    def _async_add_backup_agent_platform(self, integration_domain: str, platform: BackupAgentPlatformProtocol) -> None: ...
    async def _async_reload_backup_agents(self, domain: str) -> None: ...
    async def _add_platform(self, hass: HomeAssistant, integration_domain: str, platform: Any) -> None: ...
    async def async_pre_backup_actions(self) -> None: ...
    async def async_post_backup_actions(self) -> None: ...
    async def load_platforms(self) -> None: ...
    async def _async_upload_backup(self, *, backup: AgentBackup, agent_ids: list[str], open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]]) -> dict[str, Exception]: ...
    async def async_get_backups(self) -> tuple[dict[str, ManagerBackup], dict[str, Exception]]: ...
    async def async_get_backup(self, backup_id: str) -> tuple[ManagerBackup | None, dict[str, Exception]]: ...
    @staticmethod
    def is_our_automatic_backup(backup: AgentBackup, our_instance_id: str) -> bool | None: ...
    async def async_delete_backup(self, backup_id: str) -> dict[str, Exception]: ...
    async def async_receive_backup(self, *, agent_ids: list[str], contents: aiohttp.BodyPartReader) -> None: ...
    async def _async_receive_backup(self, *, agent_ids: list[str], contents: aiohttp.BodyPartReader) -> None: ...
    async def async_create_backup(self, *, agent_ids: list[str], include_addons: list[str] | None, include_all_addons: bool, include_database: bool, include_folders: list[Folder] | None, include_homeassistant: bool, name: str | None, password: str | None, with_automatic_settings: bool = False) -> NewBackup: ...
    async def async_initiate_backup(self, *, agent_ids: list[str], include_addons: list[str] | None, include_all_addons: bool, include_database: bool, include_folders: list[Folder] | None, include_homeassistant: bool, name: str | None, password: str | None, raise_task_error: bool = False, with_automatic_settings: bool = False) -> NewBackup: ...
    async def _async_create_backup(self, *, agent_ids: list[str], include_addons: list[str] | None, include_all_addons: bool, include_database: bool, include_folders: list[Folder] | None, include_homeassistant: bool, name: str | None, password: str | None, raise_task_error: bool, with_automatic_settings: bool) -> NewBackup: ...
    async def _async_finish_backup(self, agent_ids: list[str], with_automatic_settings: bool) -> None: ...
    async def async_restore_backup(self, backup_id: str, *, agent_id: str, password: str | None, restore_addons: list[str] | None, restore_database: bool, restore_folders: list[Folder] | None, restore_homeassistant: bool) -> None: ...
    async def _async_restore_backup(self, backup_id: str, *, agent_id: str, password: str | None, restore_addons: list[str] | None, restore_database: bool, restore_folders: list[Folder] | None, restore_homeassistant: bool) -> None: ...
    @callback
    def async_on_backup_event(self, event: ManagerStateEvent) -> None: ...
    @callback
    def async_subscribe_events(self, on_event: Callable[[ManagerStateEvent], None]) -> Callable[[], None]: ...
    def _update_issue_backup_failed(self) -> None: ...
    def _update_issue_after_agent_upload(self, agent_errors: dict[str, Exception]) -> None: ...

class KnownBackups:
    _backups: dict[str, KnownBackup]
    _manager: Incomplete
    def __init__(self, manager: BackupManager) -> None: ...
    def load(self, stored_backups: list[StoredKnownBackup]) -> None: ...
    def to_list(self) -> list[StoredKnownBackup]: ...
    def add(self, backup: AgentBackup, agent_errors: dict[str, Exception]) -> None: ...
    def get(self, backup_id: str) -> KnownBackup | None: ...
    def remove(self, backup_id: str) -> None: ...

@dataclass(kw_only=True)
class KnownBackup:
    backup_id: str
    failed_agent_ids: list[str]
    def to_dict(self) -> StoredKnownBackup: ...

class StoredKnownBackup(TypedDict):
    backup_id: str
    failed_agent_ids: list[str]

class CoreBackupReaderWriter(BackupReaderWriter):
    _local_agent_id: Incomplete
    _hass: Incomplete
    temp_backup_dir: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_create_backup(self, *, agent_ids: list[str], backup_name: str, extra_metadata: dict[str, bool | str], include_addons: list[str] | None, include_all_addons: bool, include_database: bool, include_folders: list[Folder] | None, include_homeassistant: bool, on_progress: Callable[[ManagerStateEvent], None], password: str | None) -> tuple[NewBackup, asyncio.Task[WrittenBackup]]: ...
    async def _async_create_backup(self, *, agent_ids: list[str], backup_id: str, backup_name: str, date_str: str, extra_metadata: dict[str, bool | str], include_database: bool, on_progress: Callable[[ManagerStateEvent], None], password: str | None) -> WrittenBackup: ...
    def _mkdir_and_generate_backup_contents(self, backup_data: dict[str, Any], database_included: bool, password: str | None, tar_file_path: Path | None) -> tuple[Path, int]: ...
    async def async_receive_backup(self, *, agent_ids: list[str], stream: AsyncIterator[bytes], suggested_filename: str) -> WrittenBackup: ...
    async def async_restore_backup(self, backup_id: str, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], *, agent_id: str, password: str | None, restore_addons: list[str] | None, restore_database: bool, restore_folders: list[Folder] | None, restore_homeassistant: bool) -> None: ...

def _generate_backup_id(date: str, name: str) -> str: ...
