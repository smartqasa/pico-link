from .const import CONF_CATEGORIES as CONF_CATEGORIES, CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from holidays import HolidayBase as HolidayBase
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time

def _get_obj_holidays_and_language(country: str, province: str | None, language: str, selected_categories: list[str] | None) -> tuple[HolidayBase, str]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HolidayCalendarEntity(CalendarEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_event: CalendarEvent | None
    _attr_should_poll: bool
    unsub: CALLBACK_TYPE | None
    _country: Incomplete
    _province: Incomplete
    _location: Incomplete
    _language: Incomplete
    _categories: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _obj_holidays: Incomplete
    def __init__(self, name: str, country: str, province: str | None, language: str, categories: list[str] | None, obj_holidays: HolidayBase, unique_id: str) -> None: ...
    def get_next_interval(self, now: datetime) -> datetime: ...
    def _update_state_and_setup_listener(self) -> None: ...
    @callback
    def point_in_time_listener(self, time_date: datetime) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_event(self, now: datetime) -> CalendarEvent | None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
