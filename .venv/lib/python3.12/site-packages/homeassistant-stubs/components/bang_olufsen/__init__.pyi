from .const import DOMAIN as DOMAIN
from .websocket import BangOlufsenWebsocket as BangOlufsenWebsocket
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.util.ssl import get_default_context as get_default_context
from mozart_api.mozart_client import MozartClient

@dataclass
class BangOlufsenData:
    websocket: BangOlufsenWebsocket
    client: MozartClient
type BangOlufsenConfigEntry = ConfigEntry[BangOlufsenData]

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BangOlufsenConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BangOlufsenConfigEntry) -> bool: ...
