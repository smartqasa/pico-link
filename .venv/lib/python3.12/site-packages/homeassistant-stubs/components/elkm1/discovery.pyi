from .const import DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from elkm1_lib.discovery import ElkSystem
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow

_LOGGER: Incomplete

def _short_mac(mac_address: str) -> str: ...
@callback
def async_update_entry_from_discovery(hass: HomeAssistant, entry: config_entries.ConfigEntry, device: ElkSystem) -> bool: ...
async def async_discover_devices(hass: HomeAssistant, timeout: int, address: str | None = None) -> list[ElkSystem]: ...
async def async_discover_device(hass: HomeAssistant, host: str) -> ElkSystem | None: ...
@callback
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: list[ElkSystem]) -> None: ...
