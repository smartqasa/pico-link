from _typeshed import Incomplete
from homeassistant.components.humidifier import HumidifierDeviceClass as HumidifierDeviceClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.device import async_remove_stale_devices_links_keep_entity_device as async_remove_stale_devices_links_keep_entity_device
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
CONF_HUMIDIFIER: str
CONF_SENSOR: str
CONF_MIN_HUMIDITY: str
CONF_MAX_HUMIDITY: str
CONF_TARGET_HUMIDITY: str
CONF_DEVICE_CLASS: str
CONF_MIN_DUR: str
CONF_DRY_TOLERANCE: str
CONF_WET_TOLERANCE: str
CONF_KEEP_ALIVE: str
CONF_INITIAL_STATE: str
CONF_AWAY_HUMIDITY: str
CONF_AWAY_FIXED: str
CONF_STALE_DURATION: str
DEFAULT_TOLERANCE: int
DEFAULT_NAME: str
HYGROSTAT_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def config_entry_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
