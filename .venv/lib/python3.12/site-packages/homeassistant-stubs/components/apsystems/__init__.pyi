from .const import DEFAULT_PORT as DEFAULT_PORT
from .coordinator import ApSystemsDataCoordinator as ApSystemsDataCoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

@dataclass
class ApSystemsData:
    coordinator: ApSystemsDataCoordinator
    device_id: str
type ApSystemsConfigEntry = ConfigEntry[ApSystemsData]

async def async_setup_entry(hass: HomeAssistant, entry: ApSystemsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
