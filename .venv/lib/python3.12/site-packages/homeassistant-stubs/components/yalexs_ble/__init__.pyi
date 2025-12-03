from .const import CONF_ALWAYS_CONNECTED as CONF_ALWAYS_CONNECTED, CONF_KEY as CONF_KEY, CONF_LOCAL_NAME as CONF_LOCAL_NAME, CONF_SLOT as CONF_SLOT, DEVICE_TIMEOUT as DEVICE_TIMEOUT
from .models import YaleXSBLEData as YaleXSBLEData
from .util import async_find_existing_service_info as async_find_existing_service_info, bluetooth_callback_matcher as bluetooth_callback_matcher
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from yalexs_ble import ConnectionInfo as ConnectionInfo, LockInfo as LockInfo, LockState as LockState

type YALEXSBLEConfigEntry = ConfigEntry[YaleXSBLEData]
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: YALEXSBLEConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: YALEXSBLEConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: YALEXSBLEConfigEntry) -> bool: ...
