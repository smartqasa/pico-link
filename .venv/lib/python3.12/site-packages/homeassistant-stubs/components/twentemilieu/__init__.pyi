from .coordinator import TwenteMilieuConfigEntry as TwenteMilieuConfigEntry, TwenteMilieuDataUpdateCoordinator as TwenteMilieuDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_ID as CONF_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

SERVICE_UPDATE: str
SERVICE_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TwenteMilieuConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TwenteMilieuConfigEntry) -> bool: ...
