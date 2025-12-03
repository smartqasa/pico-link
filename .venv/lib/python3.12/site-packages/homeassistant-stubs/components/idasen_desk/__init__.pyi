from .coordinator import IdasenDeskCoordinator as IdasenDeskCoordinator
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
_LOGGER: Incomplete
type IdasenDeskConfigEntry = ConfigEntry[IdasenDeskCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: IdasenDeskConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: IdasenDeskConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: IdasenDeskConfigEntry) -> bool: ...
