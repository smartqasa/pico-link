from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBeeCoordinator as SwitchBeeCoordinator
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from switchbee.api import CentralUnitPolling, CentralUnitWsRPC

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def get_api_object(central_unit: str, user: str, password: str, websession: ClientSession) -> CentralUnitPolling | CentralUnitWsRPC: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
