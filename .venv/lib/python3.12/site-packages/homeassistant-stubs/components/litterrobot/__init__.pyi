from .const import DOMAIN as DOMAIN
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from pylitterbot import Robot

type LitterRobotConfigEntry = ConfigEntry[LitterRobotHub]
PLATFORMS_BY_TYPE: Incomplete

def get_platforms_for_robots(robots: list[Robot]) -> set[Platform]: ...
async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: LitterRobotConfigEntry, device_entry: DeviceEntry) -> bool: ...
