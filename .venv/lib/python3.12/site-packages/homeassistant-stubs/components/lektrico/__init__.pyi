from .coordinator import LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

CHARGERS_PLATFORMS: list[Platform]
LB_DEVICES_PLATFORMS: list[Platform]
type LektricoConfigEntry = ConfigEntry[LektricoDeviceDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: LektricoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _get_platforms(entry: ConfigEntry) -> list[Platform]: ...
