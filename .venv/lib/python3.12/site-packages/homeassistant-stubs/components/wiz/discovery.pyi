from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow
from pywizlight.discovery import DiscoveredBulb

_LOGGER: Incomplete

async def async_discover_devices(hass: HomeAssistant, timeout: int) -> list[DiscoveredBulb]: ...
@callback
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: list[DiscoveredBulb]) -> None: ...
