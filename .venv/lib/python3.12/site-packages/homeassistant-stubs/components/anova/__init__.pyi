from .coordinator import AnovaCoordinator as AnovaCoordinator
from .models import AnovaConfigEntry as AnovaConfigEntry, AnovaData as AnovaData
from _typeshed import Incomplete
from anova_wifi import APCWifiDevice as APCWifiDevice
from homeassistant.const import CONF_DEVICES as CONF_DEVICES, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AnovaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AnovaConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: AnovaConfigEntry) -> bool: ...
