from .const import CONF_AFTER_OFFSET as CONF_AFTER_OFFSET, CONF_AFTER_TIME as CONF_AFTER_TIME, CONF_BEFORE_OFFSET as CONF_BEFORE_OFFSET, CONF_BEFORE_TIME as CONF_BEFORE_TIME
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime, time, timedelta
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_AFTER as CONF_AFTER, CONF_BEFORE as CONF_BEFORE, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date, get_astral_event_next as get_astral_event_next
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Literal, TypeGuard

type SunEventType = Literal['sunrise', 'sunset']
_LOGGER: Incomplete
ATTR_AFTER: str
ATTR_BEFORE: str
ATTR_NEXT_UPDATE: str
PLATFORM_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
def _is_sun_event(sun_event: time | SunEventType) -> TypeGuard[SunEventType]: ...

class TodSensor(BinarySensorEntity):
    _attr_should_poll: bool
    _time_before: datetime
    _time_after: datetime
    _next_update: datetime
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _after_offset: Incomplete
    _before_offset: Incomplete
    _before: Incomplete
    _after: Incomplete
    _unsub_update: Callable[[], None] | None
    def __init__(self, name: str, after: time, after_offset: timedelta, before: time, before_offset: timedelta, unique_id: str | None) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    def _naive_time_to_utc_datetime(self, naive_time: time) -> datetime: ...
    def _calculate_boundary_time(self) -> None: ...
    def _add_one_dst_aware_day(self, a_date: datetime, target_time: time) -> datetime: ...
    def _turn_to_next_day(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _calculate_next_update(self) -> None: ...
    @callback
    def _point_in_time_listener(self, now: datetime) -> None: ...
