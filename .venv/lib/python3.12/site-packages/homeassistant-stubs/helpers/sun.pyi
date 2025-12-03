import astral
import astral.location
import datetime
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.const import SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey

DATA_LOCATION_CACHE: HassKey[dict[tuple[str, str, str, float, float], astral.location.Location]]
ELEVATION_AGNOSTIC_EVENTS: Incomplete
type _AstralSunEventCallable = Callable[..., datetime.datetime]

@callback
@bind_hass
def get_astral_location(hass: HomeAssistant) -> tuple[astral.location.Location, astral.Elevation]: ...
@callback
@bind_hass
def get_astral_event_next(hass: HomeAssistant, event: str, utc_point_in_time: datetime.datetime | None = None, offset: datetime.timedelta | None = None) -> datetime.datetime: ...
@callback
def get_location_astral_event_next(location: astral.location.Location, elevation: astral.Elevation, event: str, utc_point_in_time: datetime.datetime | None = None, offset: datetime.timedelta | None = None) -> datetime.datetime: ...
@callback
@bind_hass
def get_astral_event_date(hass: HomeAssistant, event: str, date: datetime.date | datetime.datetime | None = None) -> datetime.datetime | None: ...
@callback
@bind_hass
def is_up(hass: HomeAssistant, utc_point_in_time: datetime.datetime | None = None) -> bool: ...
