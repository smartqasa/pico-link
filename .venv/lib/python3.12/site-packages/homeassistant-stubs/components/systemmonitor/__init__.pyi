import psutil_home_assistant as ha_psutil
from .coordinator import SystemMonitorCoordinator as SystemMonitorCoordinator
from .util import get_all_disk_mounts as get_all_disk_mounts
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: Incomplete
type SystemMonitorConfigEntry = ConfigEntry[SystemMonitorData]

@dataclass
class SystemMonitorData:
    coordinator: SystemMonitorCoordinator
    psutil_wrapper: ha_psutil.PsutilWrapper

async def async_setup_entry(hass: HomeAssistant, entry: SystemMonitorConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
