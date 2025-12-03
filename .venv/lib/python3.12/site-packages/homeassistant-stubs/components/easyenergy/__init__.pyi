from .const import DOMAIN as DOMAIN
from .coordinator import EasyEnergyConfigEntry as EasyEnergyConfigEntry, EasyEnergyDataUpdateCoordinator as EasyEnergyDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: EasyEnergyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EasyEnergyConfigEntry) -> bool: ...
