from .const import CONF_USE_HTTPS as CONF_USE_HTTPS, DOMAIN as DOMAIN
from .exceptions import PasswordIncompatible as PasswordIncompatible, ReolinkException as ReolinkException, UserNotAdmin as UserNotAdmin
from .host import ReolinkHost as ReolinkHost
from .services import async_setup_services as async_setup_services
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData, get_device_uid_and_ch as get_device_uid_and_ch
from .views import PlaybackProxyView as PlaybackProxyView
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
PLATFORMS: Incomplete
DEVICE_UPDATE_INTERVAL: Incomplete
FIRMWARE_UPDATE_INTERVAL: Incomplete
NUM_CRED_ERRORS: int
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry) -> bool: ...
async def entry_update_listener(hass: HomeAssistant, config_entry: ReolinkConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ReolinkConfigEntry, device: dr.DeviceEntry) -> bool: ...
def migrate_entity_ids(hass: HomeAssistant, config_entry_id: str, host: ReolinkHost) -> None: ...
