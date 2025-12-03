from .api import PushBulletNotificationProvider as PushBulletNotificationProvider
from .const import DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
