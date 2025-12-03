from . import AutomowerConfigEntry as AutomowerConfigEntry
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerBaseEntity as AutomowerBaseEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerCalendarEntity(AutomowerBaseEntity, CalendarEntity):
    _attr_name: str | None
    _attr_unique_id: Incomplete
    _event: CalendarEvent | None
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
