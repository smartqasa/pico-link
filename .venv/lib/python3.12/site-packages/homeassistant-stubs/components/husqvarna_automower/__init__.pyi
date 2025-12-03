from . import api as api
from .const import DOMAIN as DOMAIN
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow

_LOGGER: Incomplete
PLATFORMS: list[Platform]
type AutomowerConfigEntry = ConfigEntry[AutomowerDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AutomowerConfigEntry) -> bool: ...
def cleanup_removed_devices(hass: HomeAssistant, config_entry: AutomowerConfigEntry, available_devices: list[str]) -> None: ...
def remove_work_area_entities(hass: HomeAssistant, config_entry: AutomowerConfigEntry, removed_work_areas: set[int], mower_id: str) -> None: ...
