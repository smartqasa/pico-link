from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, CONF_APP_KEY as CONF_APP_KEY, LOGGER as LOGGER, TYPE_SOLARRADIATION as TYPE_SOLARRADIATION, TYPE_SOLARRADIATION_LX as TYPE_SOLARRADIATION_LX
from _typeshed import Incomplete
from aioambient import Websocket
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION, ATTR_NAME as ATTR_NAME, CONF_API_KEY as CONF_API_KEY, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from typing import Any

PLATFORMS: Incomplete
DATA_CONFIG: str
DEFAULT_SOCKET_MIN_RETRY: int
type AmbientStationConfigEntry = ConfigEntry[AmbientStation]

@callback
def async_wm2_to_lx(value: float) -> int: ...
@callback
def async_hydrate_station_data(data: dict[str, Any]) -> dict[str, Any]: ...
async def async_setup_entry(hass: HomeAssistant, entry: AmbientStationConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AmbientStationConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AmbientStation:
    _entry: Incomplete
    _entry_setup_complete: bool
    _hass: Incomplete
    _ws_reconnect_delay: Incomplete
    stations: dict[str, dict]
    websocket: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, websocket: Websocket) -> None: ...
    async def ws_connect(self) -> None: ...
    async def ws_disconnect(self) -> None: ...
