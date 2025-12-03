import asyncio
from .const import DOMAIN as DOMAIN
from .services import setup_services as setup_services
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, PlatformNotReady as PlatformNotReady
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.helpers.typing import ConfigType as ConfigType
from velbusaio.controller import Velbus

_LOGGER: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
type VelbusConfigEntry = ConfigEntry[VelbusData]

@dataclass
class VelbusData:
    controller: Velbus
    scan_task: asyncio.Task

async def velbus_scan_task(controller: Velbus, hass: HomeAssistant, entry_id: str) -> None: ...
def _migrate_device_identifiers(hass: HomeAssistant, entry_id: str) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VelbusConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: VelbusConfigEntry) -> None: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: VelbusConfigEntry) -> bool: ...
