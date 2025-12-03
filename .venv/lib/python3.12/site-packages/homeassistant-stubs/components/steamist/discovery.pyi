from .const import DISCOVERY as DISCOVERY, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from discovery30303 import Device30303 as Device30303
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.const import CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.util.network import is_ip_address as is_ip_address

_LOGGER: Incomplete
MODEL_450_HOSTNAME_PREFIX: str
MODEL_550_HOSTNAME_PREFIX: str

@callback
def async_is_steamist_device(device: Device30303) -> bool: ...
@callback
def async_update_entry_from_discovery(hass: HomeAssistant, entry: config_entries.ConfigEntry, device: Device30303) -> bool: ...
async def async_discover_devices(hass: HomeAssistant, timeout: int, address: str | None = None) -> list[Device30303]: ...
@callback
def async_find_discovery_by_ip(discoveries: list[Device30303], host: str) -> Device30303 | None: ...
async def async_discover_device(hass: HomeAssistant, host: str) -> Device30303 | None: ...
@callback
def async_get_discovery(hass: HomeAssistant, host: str) -> Device30303 | None: ...
@callback
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: list[Device30303]) -> None: ...
