import datetime
from .const import DOMAIN as DOMAIN
from .entity import ReCollectWasteEntity as ReCollectWasteEntity
from .util import async_get_pickup_type_names as async_get_pickup_type_names
from _typeshed import Incomplete
from aiorecollect.client import PickupEvent as PickupEvent
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

@callback
def async_get_calendar_event_from_pickup_event(entry: ConfigEntry, pickup_event: PickupEvent) -> CalendarEvent: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReCollectWasteCalendar(ReCollectWasteEntity, CalendarEntity):
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _event: CalendarEvent | None
    def __init__(self, coordinator: DataUpdateCoordinator[list[PickupEvent]], entry: ConfigEntry) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime.datetime, end_date: datetime.datetime) -> list[CalendarEvent]: ...
