from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from aiovlc.client import Client
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

PLATFORMS: Incomplete
type VlcConfigEntry = ConfigEntry[VlcData]

@dataclass
class VlcData:
    vlc: Client
    available: bool

async def async_setup_entry(hass: HomeAssistant, entry: VlcConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
