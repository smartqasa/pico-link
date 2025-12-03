from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_IDENTITY as CONF_IDENTITY, CONF_KEY as CONF_KEY, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, FACTORY as FACTORY, KEY_API as KEY_API, LOGGER as LOGGER
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device

PLATFORMS: Incomplete
SIGNAL_GW: str
TIMEOUT_API: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
@callback
def remove_stale_devices(hass: HomeAssistant, config_entry: ConfigEntry, devices: list[Device]) -> None: ...
