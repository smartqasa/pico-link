from .const import SIGNAL_EVENTS_CHANGED as SIGNAL_EVENTS_CHANGED, SIGNAL_POSITION_CHANGED as SIGNAL_POSITION_CHANGED, STATE_ABOVE_HORIZON as STATE_ABOVE_HORIZON, STATE_BELOW_HORIZON as STATE_BELOW_HORIZON
from _typeshed import Incomplete
from astral.location import Elevation as Elevation, Location as Location
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.sun import get_astral_location as get_astral_location, get_location_astral_event_next as get_location_astral_event_next
from typing import Any

type SunConfigEntry = ConfigEntry[Sun]
_LOGGER: Incomplete
ENTITY_ID: str
STATE_ATTR_AZIMUTH: str
STATE_ATTR_ELEVATION: str
STATE_ATTR_RISING: str
STATE_ATTR_NEXT_DAWN: str
STATE_ATTR_NEXT_DUSK: str
STATE_ATTR_NEXT_MIDNIGHT: str
STATE_ATTR_NEXT_NOON: str
STATE_ATTR_NEXT_RISING: str
STATE_ATTR_NEXT_SETTING: str
PHASE_NIGHT: str
PHASE_ASTRONOMICAL_TWILIGHT: str
PHASE_NAUTICAL_TWILIGHT: str
PHASE_TWILIGHT: str
PHASE_SMALL_DAY: str
PHASE_DAY: str
_PHASE_UPDATES: Incomplete

class Sun(Entity):
    _unrecorded_attributes: Incomplete
    _attr_name: str
    entity_id = ENTITY_ID
    location: Location
    elevation: Elevation
    next_rising: datetime
    next_setting: datetime
    next_dawn: datetime
    next_dusk: datetime
    next_midnight: datetime
    next_noon: datetime
    solar_elevation: float
    solar_azimuth: float
    rising: bool
    _next_change: datetime
    hass: Incomplete
    phase: str | None
    _config_listener: CALLBACK_TYPE | None
    _update_events_listener: CALLBACK_TYPE | None
    _update_sun_position_listener: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def update_location(self, _: Event | None = None, initial: bool = False) -> None: ...
    @callback
    def remove_listeners(self) -> None: ...
    @property
    def state(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _check_event(self, utc_point_in_time: datetime, sun_event: str, before: str | None) -> datetime: ...
    @callback
    def update_events(self, now: datetime | None = None) -> None: ...
    @callback
    def update_sun_position(self, now: datetime | None = None) -> None: ...
