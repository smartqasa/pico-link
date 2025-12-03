from .const import CONF_API_TYPE as CONF_API_TYPE, CONF_HUB as CONF_HUB, DOMAIN as DOMAIN, LOGGER as LOGGER, OVERKIZ_DEVICE_TO_PLATFORM as OVERKIZ_DEVICE_TO_PLATFORM, PLATFORMS as PLATFORMS, UPDATE_INTERVAL as UPDATE_INTERVAL, UPDATE_INTERVAL_ALL_ASSUMED_STATE as UPDATE_INTERVAL_ALL_ASSUMED_STATE
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from collections import defaultdict
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from pyoverkiz.client import OverkizClient
from pyoverkiz.models import Device as Device, OverkizServer as OverkizServer, Scenario as Scenario

@dataclass
class HomeAssistantOverkizData:
    coordinator: OverkizDataUpdateCoordinator
    platforms: defaultdict[Platform, list[Device]]
    scenarios: list[Scenario]
type OverkizDataConfigEntry = ConfigEntry[HomeAssistantOverkizData]

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry) -> bool: ...
async def _async_migrate_entries(hass: HomeAssistant, config_entry: OverkizDataConfigEntry) -> bool: ...
def create_local_client(hass: HomeAssistant, host: str, token: str, verify_ssl: bool) -> OverkizClient: ...
def create_cloud_client(hass: HomeAssistant, username: str, password: str, server: OverkizServer) -> OverkizClient: ...
