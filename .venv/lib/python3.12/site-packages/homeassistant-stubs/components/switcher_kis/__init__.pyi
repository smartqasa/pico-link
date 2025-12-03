from .const import DOMAIN as DOMAIN
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from _typeshed import Incomplete
from aioswitcher.device import SwitcherBase as SwitcherBase
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr

PLATFORMS: Incomplete
_LOGGER: Incomplete
type SwitcherConfigEntry = ConfigEntry[dict[str, SwitcherDataUpdateCoordinator]]

async def async_setup_entry(hass: HomeAssistant, entry: SwitcherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SwitcherConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: SwitcherConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
