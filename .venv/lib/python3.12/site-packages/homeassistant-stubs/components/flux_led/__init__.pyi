from .const import CONF_WHITE_CHANNEL_TYPE as CONF_WHITE_CHANNEL_TYPE, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN, FLUX_LED_DISCOVERY as FLUX_LED_DISCOVERY, FLUX_LED_DISCOVERY_SIGNAL as FLUX_LED_DISCOVERY_SIGNAL, FLUX_LED_EXCEPTIONS as FLUX_LED_EXCEPTIONS, SIGNAL_STATE_UPDATED as SIGNAL_STATE_UPDATED
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .discovery import async_build_cached_discovery as async_build_cached_discovery, async_clear_discovery_cache as async_clear_discovery_cache, async_discover_device as async_discover_device, async_discover_devices as async_discover_devices, async_get_discovery as async_get_discovery, async_trigger_discovery as async_trigger_discovery, async_update_entry_from_discovery as async_update_entry_from_discovery
from .util import mac_matches_by_one as mac_matches_by_one
from _typeshed import Incomplete
from flux_led.aio import AIOWifiLedBulb
from flux_led.scanner import FluxLEDDiscovery as FluxLEDDiscovery
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_change as async_track_time_change, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_LOGGER: Incomplete
PLATFORMS_BY_TYPE: Final[Incomplete]
DISCOVERY_INTERVAL: Final[Incomplete]
REQUEST_REFRESH_DELAY: Final[float]
NAME_TO_WHITE_CHANNEL_TYPE: Final[Incomplete]
CONFIG_SCHEMA: Incomplete

@callback
def async_wifi_bulb_for_host(host: str, discovery: FluxLEDDiscovery | None) -> AIOWifiLedBulb: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_migrate_unique_ids(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
