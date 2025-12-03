from .const import DOMAIN as DOMAIN, METEO_UPDATE_INTERVAL as METEO_UPDATE_INTERVAL, PLATFORMS as PLATFORMS, REMOTE_UPDATE_INTERVAL as REMOTE_UPDATE_INTERVAL, TYPE_TO_PLATFORM as TYPE_TO_PLATFORM
from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator, LookinPushCoordinator as LookinPushCoordinator
from .models import LookinData as LookinData
from _typeshed import Incomplete
from aiolookin import Climate as Climate, LookInHttpProtocol, LookinUDPSubscriptions, Remote as Remote
from aiolookin.models import UDPEvent as UDPEvent
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

LOGGER: Incomplete
UDP_MANAGER: str

def _async_climate_updater(lookin_protocol: LookInHttpProtocol, uuid: str) -> Callable[[], Coroutine[None, Any, Remote]]: ...
def _async_remote_updater(lookin_protocol: LookInHttpProtocol, uuid: str) -> Callable[[], Coroutine[None, Any, Remote]]: ...

class LookinUDPManager:
    _lock: Incomplete
    _listener: Callable | None
    _subscriptions: LookinUDPSubscriptions | None
    def __init__(self) -> None: ...
    async def async_get_subscriptions(self) -> LookinUDPSubscriptions: ...
    async def async_stop(self) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
