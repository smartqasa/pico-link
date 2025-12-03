import dataclasses
from .const import CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE as CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE, DATA_UPCLOUD as DATA_UPCLOUD, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from .coordinator import UpCloudDataUpdateCoordinator as UpCloudDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send

_LOGGER: Incomplete
PLATFORMS: Incomplete

@dataclasses.dataclass
class UpCloudHassData:
    coordinators: dict[str, UpCloudDataUpdateCoordinator] = dataclasses.field(default_factory=dict)

def _config_entry_update_signal_name(config_entry: ConfigEntry) -> str: ...
async def _async_signal_options_update(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
