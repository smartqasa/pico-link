from .const import PLATFORMS as PLATFORMS
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .hub import AxisHub as AxisHub, get_axis_api as get_axis_api
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
type AxisConfigEntry = ConfigEntry[AxisHub]

async def async_setup_entry(hass: HomeAssistant, config_entry: AxisConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
