from .const import SIGNAL_THERMOSTAT_CONNECTED as SIGNAL_THERMOSTAT_CONNECTED, SIGNAL_THERMOSTAT_DISCONNECTED as SIGNAL_THERMOSTAT_DISCONNECTED
from .models import Eq3Config as Eq3Config, Eq3ConfigEntryData as Eq3ConfigEntryData
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

PLATFORMS: Incomplete
_LOGGER: Incomplete
type Eq3ConfigEntry = ConfigEntry[Eq3ConfigEntryData]

async def async_setup_entry(hass: HomeAssistant, entry: Eq3ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: Eq3ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: Eq3ConfigEntry) -> None: ...
async def _async_run_thermostat(hass: HomeAssistant, entry: Eq3ConfigEntry) -> None: ...
async def _async_reconnect_thermostat(hass: HomeAssistant, entry: Eq3ConfigEntry) -> None: ...
