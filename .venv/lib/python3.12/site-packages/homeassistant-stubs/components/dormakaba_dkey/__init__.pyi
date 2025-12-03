from .const import CONF_ASSOCIATION_DATA as CONF_ASSOCIATION_DATA, DOMAIN as DOMAIN, UPDATE_SECONDS as UPDATE_SECONDS
from .models import DormakabaDkeyData as DormakabaDkeyData
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
