from .coordinator import AsekoConfigEntry as AsekoConfigEntry, AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

_LOGGER: Incomplete
PLATFORMS: list[str]

async def async_setup_entry(hass: HomeAssistant, entry: AsekoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AsekoConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: AsekoConfigEntry) -> bool: ...
