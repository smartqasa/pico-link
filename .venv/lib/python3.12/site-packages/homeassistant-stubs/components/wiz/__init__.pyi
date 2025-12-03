from .const import DISCOVERY_INTERVAL as DISCOVERY_INTERVAL, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN, SIGNAL_WIZ_PIR as SIGNAL_WIZ_PIR, WIZ_CONNECT_EXCEPTIONS as WIZ_CONNECT_EXCEPTIONS, WIZ_EXCEPTIONS as WIZ_EXCEPTIONS
from .discovery import async_discover_devices as async_discover_devices, async_trigger_discovery as async_trigger_discovery
from .models import WizData as WizData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pywizlight import PilotParser as PilotParser

type WizConfigEntry = ConfigEntry[WizData]
_LOGGER: Incomplete
PLATFORMS: Incomplete
REQUEST_REFRESH_DELAY: float
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, hass_config: ConfigType) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
