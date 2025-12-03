from .const import DOMAIN as DOMAIN
from .coordinator import LD2410BLECoordinator as LD2410BLECoordinator
from .models import LD2410BLEData as LD2410BLEData
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
