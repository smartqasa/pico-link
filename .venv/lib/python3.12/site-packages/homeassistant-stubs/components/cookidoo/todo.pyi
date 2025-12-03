from .const import DOMAIN as DOMAIN
from .coordinator import CookidooConfigEntry as CookidooConfigEntry, CookidooDataUpdateCoordinator as CookidooDataUpdateCoordinator
from .entity import CookidooBaseEntity as CookidooBaseEntity
from _typeshed import Incomplete
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: CookidooConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CookidooIngredientsTodoListEntity(CookidooBaseEntity, TodoListEntity):
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CookidooDataUpdateCoordinator) -> None: ...
    @property
    def todo_items(self) -> list[TodoItem]: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...

class CookidooAdditionalItemTodoListEntity(CookidooBaseEntity, TodoListEntity):
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CookidooDataUpdateCoordinator) -> None: ...
    @property
    def todo_items(self) -> list[TodoItem]: ...
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
