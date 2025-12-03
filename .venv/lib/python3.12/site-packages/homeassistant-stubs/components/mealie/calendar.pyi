from .coordinator import MealieConfigEntry as MealieConfigEntry, MealieMealplanCoordinator as MealieMealplanCoordinator
from .entity import MealieEntity as MealieEntity
from _typeshed import Incomplete
from aiomealie import Mealplan as Mealplan, MealplanEntryType
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: MealieConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _get_event_from_mealplan(mealplan: Mealplan) -> CalendarEvent: ...

class MealieMealplanCalendarEntity(MealieEntity, CalendarEntity):
    _entry_type: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: MealieMealplanCoordinator, entry_type: MealplanEntryType) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
