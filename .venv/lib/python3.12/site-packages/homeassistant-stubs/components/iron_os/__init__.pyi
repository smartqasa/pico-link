from .const import DOMAIN as DOMAIN
from .coordinator import IronOSCoordinators as IronOSCoordinators, IronOSFirmwareUpdateCoordinator as IronOSFirmwareUpdateCoordinator, IronOSLiveDataCoordinator as IronOSLiveDataCoordinator, IronOSSettingsCoordinator as IronOSSettingsCoordinator
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete
type IronOSConfigEntry = ConfigEntry[IronOSCoordinators]
IRON_OS_KEY: HassKey[IronOSFirmwareUpdateCoordinator]
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IronOSConfigEntry) -> bool: ...
