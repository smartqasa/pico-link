from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import __version__ as __version__
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from radios import RadioBrowser

type RadioBrowserConfigEntry = ConfigEntry[RadioBrowser]
async def async_setup_entry(hass: HomeAssistant, entry: RadioBrowserConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
