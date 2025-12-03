from _typeshed import Incomplete
from homeassistant.components import camera as camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from rtsp_to_webrtc.interface import WebRTCClientInterface as WebRTCClientInterface

_LOGGER: Incomplete
DOMAIN: str
DATA_SERVER_URL: str
DATA_UNSUB: str
TIMEOUT: int
CONF_STUN_SERVER: str
_DEPRECATED: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
