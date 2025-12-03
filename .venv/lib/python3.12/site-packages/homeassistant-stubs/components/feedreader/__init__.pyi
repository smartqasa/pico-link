from .const import CONF_MAX_ENTRIES as CONF_MAX_ENTRIES, DOMAIN as DOMAIN
from .coordinator import FeedReaderCoordinator as FeedReaderCoordinator, StoredData as StoredData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.hass_dict import HassKey as HassKey

type FeedReaderConfigEntry = ConfigEntry[FeedReaderCoordinator]
CONF_URLS: str
MY_KEY: HassKey[StoredData]

async def async_setup_entry(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> None: ...
