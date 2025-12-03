from .const import CONF_AREAS as CONF_AREAS, DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .coordinator import NordPoolDataUpdateCoordinator as NordPoolDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

type NordPoolConfigEntry = ConfigEntry[NordPoolDataUpdateCoordinator]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: NordPoolConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: NordPoolConfigEntry) -> bool: ...
async def cleanup_device(hass: HomeAssistant, config_entry: NordPoolConfigEntry) -> None: ...
