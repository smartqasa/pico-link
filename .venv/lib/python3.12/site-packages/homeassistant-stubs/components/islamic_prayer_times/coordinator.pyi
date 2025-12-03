from .const import CONF_CALC_METHOD as CONF_CALC_METHOD, CONF_LAT_ADJ_METHOD as CONF_LAT_ADJ_METHOD, CONF_MIDNIGHT_MODE as CONF_MIDNIGHT_MODE, CONF_SCHOOL as CONF_SCHOOL, DEFAULT_CALC_METHOD as DEFAULT_CALC_METHOD, DEFAULT_LAT_ADJ_METHOD as DEFAULT_LAT_ADJ_METHOD, DEFAULT_MIDNIGHT_MODE as DEFAULT_MIDNIGHT_MODE, DEFAULT_SCHOOL as DEFAULT_SCHOOL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import date, datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_point_in_time as async_track_point_in_time
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Incomplete

class IslamicPrayerDataUpdateCoordinator(DataUpdateCoordinator[dict[str, datetime]]):
    config_entry: ConfigEntry
    latitude: Incomplete
    longitude: Incomplete
    event_unsub: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def calc_method(self) -> str: ...
    @property
    def lat_adj_method(self) -> str: ...
    @property
    def midnight_mode(self) -> str: ...
    @property
    def school(self) -> str: ...
    def get_new_prayer_times(self, for_date: date) -> dict[str, Any]: ...
    @callback
    def async_schedule_future_update(self, midnight_dt: datetime) -> None: ...
    async def async_request_update(self, _: datetime) -> None: ...
    async def _async_update_data(self) -> dict[str, datetime]: ...
