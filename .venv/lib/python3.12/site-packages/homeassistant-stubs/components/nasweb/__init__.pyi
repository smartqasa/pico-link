from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SUPPORT_EMAIL as SUPPORT_EMAIL
from .coordinator import NASwebCoordinator as NASwebCoordinator
from .nasweb_data import NASwebData as NASwebData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError
from homeassistant.util.hass_dict import HassKey as HassKey

PLATFORMS: list[Platform]
NASWEB_CONFIG_URL: str
_LOGGER: Incomplete
type NASwebConfigEntry = ConfigEntry[NASwebCoordinator]
DATA_NASWEB: HassKey[NASwebData]

async def async_setup_entry(hass: HomeAssistant, entry: NASwebConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NASwebConfigEntry) -> bool: ...
