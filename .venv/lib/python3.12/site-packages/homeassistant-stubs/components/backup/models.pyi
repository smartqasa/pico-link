from dataclasses import dataclass
from enum import StrEnum
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Self

@dataclass(frozen=True, kw_only=True)
class AddonInfo:
    name: str
    slug: str
    version: str

class Folder(StrEnum):
    SHARE = 'share'
    ADDONS = 'addons/local'
    SSL = 'ssl'
    MEDIA = 'media'

@dataclass(frozen=True, kw_only=True)
class AgentBackup:
    addons: list[AddonInfo]
    backup_id: str
    date: str
    database_included: bool
    extra_metadata: dict[str, bool | str]
    folders: list[Folder]
    homeassistant_included: bool
    homeassistant_version: str | None
    name: str
    protected: bool
    size: int
    def as_dict(self) -> dict: ...
    def as_frontend_json(self) -> dict: ...
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self: ...

class BackupManagerError(HomeAssistantError): ...
