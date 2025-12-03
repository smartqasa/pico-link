import datetime
from .const import DOMAIN as DOMAIN
from .coordinator import RidwellDataUpdateCoordinator as RidwellDataUpdateCoordinator
from .entity import RidwellEntity as RidwellEntity
from _typeshed import Incomplete
from aioridwell.model import RidwellAccount as RidwellAccount, RidwellPickupEvent as RidwellPickupEvent
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@callback
def async_get_calendar_event_from_pickup_event(pickup_event: RidwellPickupEvent) -> CalendarEvent: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RidwellCalendar(RidwellEntity, CalendarEntity):
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _event: CalendarEvent | None
    def __init__(self, coordinator: RidwellDataUpdateCoordinator, account: RidwellAccount) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime.datetime, end_date: datetime.datetime) -> list[CalendarEvent]: ...
