from .const import ALLOWED_DAYS as ALLOWED_DAYS, CONF_ADD_HOLIDAYS as CONF_ADD_HOLIDAYS, CONF_CATEGORY as CONF_CATEGORY, CONF_EXCLUDES as CONF_EXCLUDES, CONF_OFFSET as CONF_OFFSET, CONF_PROVINCE as CONF_PROVINCE, CONF_REMOVE_HOLIDAYS as CONF_REMOVE_HOLIDAYS, CONF_WORKDAYS as CONF_WORKDAYS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from datetime import date, datetime
from holidays import HolidayBase
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_LANGUAGE as CONF_LANGUAGE, CONF_NAME as CONF_NAME
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.util import slugify as slugify
from typing import Final

SERVICE_CHECK_DATE: Final[str]
CHECK_DATE: Final[str]

def validate_dates(holiday_list: list[str]) -> list[str]: ...
def _get_obj_holidays(country: str | None, province: str | None, year: int, language: str | None, categories: list[str] | None) -> HolidayBase: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IsWorkdaySensor(BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key = DOMAIN
    _attr_should_poll: bool
    unsub: CALLBACK_TYPE | None
    _obj_holidays: Incomplete
    _workdays: Incomplete
    _excludes: Incomplete
    _days_offset: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, obj_holidays: HolidayBase, workdays: list[str], excludes: list[str], days_offset: int, name: str, entry_id: str) -> None: ...
    def is_include(self, day: str, now: date) -> bool: ...
    def is_exclude(self, day: str, now: date) -> bool: ...
    def get_next_interval(self, now: datetime) -> datetime: ...
    def _update_state_and_setup_listener(self) -> None: ...
    @callback
    def point_in_time_listener(self, time_date: datetime) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    def update_data(self, now: datetime) -> None: ...
    def check_date(self, check_date: date) -> ServiceResponse: ...
    def date_is_workday(self, check_date: date) -> bool: ...
