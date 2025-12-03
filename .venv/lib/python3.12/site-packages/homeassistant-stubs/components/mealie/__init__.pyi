from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, MIN_REQUIRED_MEALIE_VERSION as MIN_REQUIRED_MEALIE_VERSION
from .coordinator import MealieConfigEntry as MealieConfigEntry, MealieData as MealieData, MealieMealplanCoordinator as MealieMealplanCoordinator, MealieShoppingListCoordinator as MealieShoppingListCoordinator, MealieStatisticsCoordinator as MealieStatisticsCoordinator
from .services import setup_services as setup_services
from .utils import create_version as create_version
from _typeshed import Incomplete
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN, CONF_HOST as CONF_HOST, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: MealieConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MealieConfigEntry) -> bool: ...
