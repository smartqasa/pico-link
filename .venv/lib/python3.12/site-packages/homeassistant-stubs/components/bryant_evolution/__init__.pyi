from . import names as names
from .const import CONF_SYSTEM_ZONE as CONF_SYSTEM_ZONE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from evolutionhttp import BryantEvolutionLocalClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FILENAME as CONF_FILENAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
type BryantEvolutionLocalClients = dict[tuple[int, int], BryantEvolutionLocalClient]
type BryantEvolutionConfigEntry = ConfigEntry[BryantEvolutionLocalClients]
_LOGGER: Incomplete

async def _can_reach_device(client: BryantEvolutionLocalClient) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: BryantEvolutionConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BryantEvolutionConfigEntry) -> bool: ...
