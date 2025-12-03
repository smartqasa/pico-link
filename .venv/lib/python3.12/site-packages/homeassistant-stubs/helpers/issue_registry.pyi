import dataclasses
from .registry import BaseRegistry as BaseRegistry
from .singleton import singleton as singleton
from .storage import Store as Store
from _typeshed import Incomplete
from datetime import datetime
from enum import StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Literal, TypedDict

DATA_REGISTRY: HassKey[IssueRegistry]
EVENT_REPAIRS_ISSUE_REGISTRY_UPDATED: EventType[EventIssueRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int

class EventIssueRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    domain: str
    issue_id: str

class IssueSeverity(StrEnum):
    CRITICAL = 'critical'
    ERROR = 'error'
    WARNING = 'warning'

@dataclasses.dataclass(slots=True, frozen=True)
class IssueEntry:
    active: bool
    breaks_in_ha_version: str | None
    created: datetime
    data: dict[str, str | int | float | None] | None
    dismissed_version: str | None
    domain: str
    is_fixable: bool | None
    is_persistent: bool
    issue_domain: str | None
    issue_id: str
    learn_more_url: str | None
    severity: IssueSeverity | None
    translation_key: str | None
    translation_placeholders: dict[str, str] | None
    def to_json(self) -> dict[str, Any]: ...

class IssueRegistryStore(Store[dict[str, list[dict[str, Any]]]]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...

class IssueRegistry(BaseRegistry):
    hass: Incomplete
    issues: dict[tuple[str, str], IssueEntry]
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_get_issue(self, domain: str, issue_id: str) -> IssueEntry | None: ...
    @callback
    def async_get_or_create(self, domain: str, issue_id: str, *, breaks_in_ha_version: str | None = None, data: dict[str, str | int | float | None] | None = None, is_fixable: bool, is_persistent: bool, issue_domain: str | None = None, learn_more_url: str | None = None, severity: IssueSeverity, translation_key: str, translation_placeholders: dict[str, str] | None = None) -> IssueEntry: ...
    @callback
    def async_delete(self, domain: str, issue_id: str) -> None: ...
    @callback
    def async_ignore(self, domain: str, issue_id: str, ignore: bool) -> IssueEntry: ...
    @callback
    def make_read_only(self) -> None: ...
    async def async_load(self) -> None: ...
    @callback
    def _data_to_save(self) -> dict[str, list[dict[str, str | None]]]: ...

@callback
def async_get(hass: HomeAssistant) -> IssueRegistry: ...
async def async_load(hass: HomeAssistant, *, read_only: bool = False) -> None: ...
@callback
def async_create_issue(hass: HomeAssistant, domain: str, issue_id: str, *, breaks_in_ha_version: str | None = None, data: dict[str, str | int | float | None] | None = None, is_fixable: bool, is_persistent: bool = False, issue_domain: str | None = None, learn_more_url: str | None = None, severity: IssueSeverity, translation_key: str, translation_placeholders: dict[str, str] | None = None) -> None: ...
def create_issue(hass: HomeAssistant, domain: str, issue_id: str, *, breaks_in_ha_version: str | None = None, data: dict[str, str | int | float | None] | None = None, is_fixable: bool, is_persistent: bool = False, issue_domain: str | None = None, learn_more_url: str | None = None, severity: IssueSeverity, translation_key: str, translation_placeholders: dict[str, str] | None = None) -> None: ...
@callback
def async_delete_issue(hass: HomeAssistant, domain: str, issue_id: str) -> None: ...
def delete_issue(hass: HomeAssistant, domain: str, issue_id: str) -> None: ...
@callback
def async_ignore_issue(hass: HomeAssistant, domain: str, issue_id: str, ignore: bool) -> None: ...
