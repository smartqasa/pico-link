from .const import CONF_MINOR_VERSION as CONF_MINOR_VERSION, CONF_MODEL_DESCRIPTION as CONF_MODEL_DESCRIPTION, CONF_MODEL_INFO as CONF_MODEL_INFO, CONF_MODEL_NUM as CONF_MODEL_NUM, CONF_REMOTE_ACCESS_ENABLED as CONF_REMOTE_ACCESS_ENABLED, CONF_REMOTE_ACCESS_HOST as CONF_REMOTE_ACCESS_HOST, CONF_REMOTE_ACCESS_PORT as CONF_REMOTE_ACCESS_PORT, DIRECTED_DISCOVERY_TIMEOUT as DIRECTED_DISCOVERY_TIMEOUT, DOMAIN as DOMAIN, FLUX_LED_DISCOVERY as FLUX_LED_DISCOVERY
from .util import format_as_flux_mac as format_as_flux_mac, mac_matches_by_one as mac_matches_by_one
from _typeshed import Incomplete
from collections.abc import Mapping
from flux_led.scanner import FluxLEDDiscovery
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.network import is_ip_address as is_ip_address
from typing import Any, Final

_LOGGER: Incomplete
CONF_TO_DISCOVERY: Final[Incomplete]

@callback
def async_build_cached_discovery(entry: ConfigEntry) -> FluxLEDDiscovery: ...
@callback
def async_name_from_discovery(device: FluxLEDDiscovery, model_num: int | None = None) -> str: ...
@callback
def async_populate_data_from_discovery(current_data: Mapping[str, Any], data_updates: dict[str, Any], device: FluxLEDDiscovery) -> None: ...
@callback
def async_update_entry_from_discovery(hass: HomeAssistant, entry: config_entries.ConfigEntry, device: FluxLEDDiscovery, model_num: int | None, allow_update_mac: bool) -> bool: ...
@callback
def async_get_discovery(hass: HomeAssistant, host: str) -> FluxLEDDiscovery | None: ...
@callback
def async_clear_discovery_cache(hass: HomeAssistant, host: str) -> None: ...
async def async_discover_devices(hass: HomeAssistant, timeout: int, address: str | None = None) -> list[FluxLEDDiscovery]: ...
async def async_discover_device(hass: HomeAssistant, host: str) -> FluxLEDDiscovery | None: ...
@callback
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: list[FluxLEDDiscovery]) -> None: ...
