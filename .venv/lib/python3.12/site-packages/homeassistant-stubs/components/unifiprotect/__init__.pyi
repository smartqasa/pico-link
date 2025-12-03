from .const import AUTH_RETRIES as AUTH_RETRIES, CONF_ALLOW_EA as CONF_ALLOW_EA, DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DOMAIN as DOMAIN, MIN_REQUIRED_PROTECT_V as MIN_REQUIRED_PROTECT_V, OUTDATED_LOG_MESSAGE as OUTDATED_LOG_MESSAGE, PLATFORMS as PLATFORMS
from .data import ProtectData as ProtectData, UFPConfigEntry as UFPConfigEntry
from .discovery import async_start_discovery as async_start_discovery
from .migrate import async_migrate_data as async_migrate_data
from .services import async_setup_services as async_setup_services
from .utils import _async_unifi_mac_from_hass as _async_unifi_mac_from_hass, async_create_api_client as async_create_api_client, async_get_devices as async_get_devices
from .views import ThumbnailProxyView as ThumbnailProxyView, VideoEventProxyView as VideoEventProxyView, VideoProxyView as VideoProxyView
from _typeshed import Incomplete
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity
from homeassistant.helpers.typing import ConfigType as ConfigType
from uiprotect.data import Bootstrap as Bootstrap
from uiprotect.test_util.anonymize import anonymize_data as anonymize_data

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete
EARLY_ACCESS_URL: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry) -> bool: ...
async def _async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, data_service: ProtectData, bootstrap: Bootstrap) -> None: ...
async def _async_options_updated(hass: HomeAssistant, entry: UFPConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: UFPConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: UFPConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
