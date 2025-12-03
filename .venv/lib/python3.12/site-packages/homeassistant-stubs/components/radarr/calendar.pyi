from . import RadarrConfigEntry as RadarrConfigEntry
from .coordinator import CalendarUpdateCoordinator as CalendarUpdateCoordinator, RadarrEvent as RadarrEvent
from .entity import RadarrEntity as RadarrEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

CALENDAR_TYPE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RadarrConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RadarrCalendarEntity(RadarrEntity, CalendarEntity):
    coordinator: CalendarUpdateCoordinator
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[RadarrEvent]: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def async_write_ha_state(self) -> None: ...
