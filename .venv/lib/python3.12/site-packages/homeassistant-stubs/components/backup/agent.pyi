import abc
from .models import AgentBackup as AgentBackup
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from pathlib import Path
from propcache import cached_property
from typing import Any, Protocol

class BackupAgentError(HomeAssistantError): ...

class BackupAgentUnreachableError(BackupAgentError):
    _message: str

class BackupAgent(abc.ABC, metaclass=abc.ABCMeta):
    domain: str
    name: str
    @cached_property
    def agent_id(self) -> str: ...
    @abc.abstractmethod
    async def async_download_backup(self, backup_id: str, **kwargs: Any) -> AsyncIterator[bytes]: ...
    @abc.abstractmethod
    async def async_upload_backup(self, *, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], backup: AgentBackup, **kwargs: Any) -> None: ...
    @abc.abstractmethod
    async def async_delete_backup(self, backup_id: str, **kwargs: Any) -> None: ...
    @abc.abstractmethod
    async def async_list_backups(self, **kwargs: Any) -> list[AgentBackup]: ...
    @abc.abstractmethod
    async def async_get_backup(self, backup_id: str, **kwargs: Any) -> AgentBackup | None: ...

class LocalBackupAgent(BackupAgent, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_backup_path(self, backup_id: str) -> Path: ...

class BackupAgentPlatformProtocol(Protocol):
    async def async_get_backup_agents(self, hass: HomeAssistant, **kwargs: Any) -> list[BackupAgent]: ...
    @callback
    def async_register_backup_agents_listener(self, hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...
