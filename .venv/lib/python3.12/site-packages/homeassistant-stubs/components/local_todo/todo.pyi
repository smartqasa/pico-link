from . import LocalTodoConfigEntry as LocalTodoConfigEntry
from .const import CONF_TODO_LIST_NAME as CONF_TODO_LIST_NAME
from .store import LocalTodoListStore as LocalTodoListStore
from _typeshed import Incomplete
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.setup import SetupPhases as SetupPhases, async_pause_setup as async_pause_setup
from ical.calendar import Calendar as Calendar
from ical.store import TodoStore
from ical.todo import Todo

_LOGGER: Incomplete
PRODID: str
PRODID_REQUIRES_MIGRATION: str
ICS_TODO_STATUS_MAP: Incomplete
ICS_TODO_STATUS_MAP_INV: Incomplete

def _migrate_calendar(calendar: Calendar) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LocalTodoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _convert_item(item: TodoItem) -> Todo: ...

class LocalTodoListEntity(TodoListEntity):
    _attr_has_entity_name: bool
    _attr_supported_features: Incomplete
    _attr_should_poll: bool
    _store: Incomplete
    _calendar: Incomplete
    _calendar_lock: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, store: LocalTodoListStore, calendar: Calendar, name: str, unique_id: str) -> None: ...
    def _new_todo_store(self) -> TodoStore: ...
    _attr_todo_items: Incomplete
    async def async_update(self) -> None: ...
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
    async def async_move_todo_item(self, uid: str, previous_uid: str | None = None) -> None: ...
    async def async_save(self) -> None: ...
