from .const import CONF_EVENTS as CONF_EVENTS, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .device import ConfiguredDoorBird as ConfiguredDoorBird
from .models import DoorBirdConfigEntry as DoorBirdConfigEntry, DoorBirdData as DoorBirdData
from .view import DoorBirdRequestView as DoorBirdRequestView
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONF_CUSTOM_URL: str
CONFIG_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: DoorBirdConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DoorBirdConfigEntry) -> bool: ...
async def _async_register_events(hass: HomeAssistant, door_station: ConfiguredDoorBird, entry: DoorBirdConfigEntry) -> bool: ...
async def _update_listener(hass: HomeAssistant, entry: DoorBirdConfigEntry) -> None: ...
