from .const import ATTR_ALTITUDE as ATTR_ALTITUDE, ATTR_CALLSIGN as ATTR_CALLSIGN, ATTR_ICAO24 as ATTR_ICAO24, ATTR_SENSOR as ATTR_SENSOR, CONF_ALTITUDE as CONF_ALTITUDE, DEFAULT_ALTITUDE as DEFAULT_ALTITUDE, DOMAIN as DOMAIN, EVENT_OPENSKY_ENTRY as EVENT_OPENSKY_ENTRY, EVENT_OPENSKY_EXIT as EVENT_OPENSKY_EXIT, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_RADIUS as CONF_RADIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from python_opensky import OpenSky, StateVector as StateVector

class OpenSkyDataUpdateCoordinator(DataUpdateCoordinator[int]):
    config_entry: ConfigEntry
    _opensky: Incomplete
    _previously_tracked: set[str] | None
    _bounding_box: Incomplete
    _altitude: Incomplete
    def __init__(self, hass: HomeAssistant, opensky: OpenSky) -> None: ...
    async def _async_update_data(self) -> int: ...
    def _handle_boundary(self, flights: set[str], event: str, metadata: dict[str, StateVector]) -> None: ...
