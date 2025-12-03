from . import DOMAIN as DOMAIN, WithingsConfigEntry as WithingsConfigEntry
from .coordinator import WithingsWorkoutDataUpdateCoordinator as WithingsWorkoutDataUpdateCoordinator
from .entity import WithingsEntity as WithingsEntity
from _typeshed import Incomplete
from aiowithings import WithingsClient as WithingsClient, WorkoutCategory as WorkoutCategory
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: WithingsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_event_name(category: WorkoutCategory) -> str: ...

class WithingsWorkoutCalendarEntity(WithingsEntity[WithingsWorkoutDataUpdateCoordinator], CalendarEntity):
    _attr_translation_key: str
    client: Incomplete
    def __init__(self, client: WithingsClient, coordinator: WithingsWorkoutDataUpdateCoordinator) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
