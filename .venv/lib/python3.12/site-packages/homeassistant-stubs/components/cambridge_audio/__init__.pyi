from .const import CONNECT_TIMEOUT as CONNECT_TIMEOUT, DOMAIN as DOMAIN, STREAM_MAGIC_EXCEPTIONS as STREAM_MAGIC_EXCEPTIONS
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
_LOGGER: Incomplete
type CambridgeAudioConfigEntry = ConfigEntry[StreamMagicClient]

async def async_setup_entry(hass: HomeAssistant, entry: CambridgeAudioConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CambridgeAudioConfigEntry) -> bool: ...
