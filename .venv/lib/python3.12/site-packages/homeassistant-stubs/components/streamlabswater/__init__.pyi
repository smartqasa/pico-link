from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsCoordinator as StreamlabsCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall

ATTR_AWAY_MODE: str
SERVICE_SET_AWAY_MODE: str
AWAY_MODE_AWAY: str
AWAY_MODE_HOME: str
CONF_LOCATION_ID: str
ISSUE_PLACEHOLDER: Incomplete
SET_AWAY_MODE_SCHEMA: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
