from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from unifi_discovery import UnifiDevice as UnifiDevice

_LOGGER: Incomplete
DISCOVERY: str
DISCOVERY_INTERVAL: Incomplete

@callback
def async_start_discovery(hass: HomeAssistant) -> None: ...
async def async_discover_devices() -> list[UnifiDevice]: ...
@callback
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: list[UnifiDevice]) -> None: ...
