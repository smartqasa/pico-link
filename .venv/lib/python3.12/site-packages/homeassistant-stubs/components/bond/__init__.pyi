from .const import BRIDGE_MAKE as BRIDGE_MAKE, DOMAIN as DOMAIN
from .models import BondData as BondData
from .utils import BondHub as BondHub
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import SLOW_UPDATE_WARNING as SLOW_UPDATE_WARNING

PLATFORMS: Incomplete
_API_TIMEOUT: Incomplete
_LOGGER: Incomplete
type BondConfigEntry = ConfigEntry[BondData]

async def async_setup_entry(hass: HomeAssistant, entry: BondConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BondConfigEntry) -> bool: ...
@callback
def _async_remove_old_device_identifiers(config_entry_id: str, device_registry: dr.DeviceRegistry, hub: BondHub) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: BondConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
