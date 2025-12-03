from .const import WASTE_TYPE_TO_DESCRIPTION as WASTE_TYPE_TO_DESCRIPTION
from .coordinator import TwenteMilieuConfigEntry as TwenteMilieuConfigEntry
from .entity import TwenteMilieuEntity as TwenteMilieuEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: TwenteMilieuConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TwenteMilieuCalendar(TwenteMilieuEntity, CalendarEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _event: CalendarEvent | None
    def __init__(self, entry: TwenteMilieuConfigEntry) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
