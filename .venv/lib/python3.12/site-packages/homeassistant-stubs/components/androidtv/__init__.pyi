from .const import CONF_ADBKEY as CONF_ADBKEY, CONF_ADB_SERVER_IP as CONF_ADB_SERVER_IP, CONF_ADB_SERVER_PORT as CONF_ADB_SERVER_PORT, CONF_SCREENCAP_INTERVAL as CONF_SCREENCAP_INTERVAL, CONF_STATE_DETECTION_RULES as CONF_STATE_DETECTION_RULES, DEFAULT_ADB_SERVER_PORT as DEFAULT_ADB_SERVER_PORT, DEVICE_ANDROIDTV as DEVICE_ANDROIDTV, DEVICE_FIRETV as DEVICE_FIRETV, PROP_ETHMAC as PROP_ETHMAC, PROP_WIFIMAC as PROP_WIFIMAC, SIGNAL_CONFIG_ENTITY as SIGNAL_CONFIG_ENTITY
from _typeshed import Incomplete
from androidtv.adb_manager.adb_manager_sync import PythonRSASigner as PythonRSASigner
from androidtv.setup_async import AndroidTVAsync as AndroidTVAsync, FireTVAsync as FireTVAsync
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from typing import Any

ADB_PYTHON_EXCEPTIONS: tuple
ADB_TCP_EXCEPTIONS: tuple
PLATFORMS: Incomplete
RELOAD_OPTIONS: Incomplete
_INVALID_MACS: Incomplete
_LOGGER: Incomplete

@dataclass
class AndroidTVRuntimeData:
    aftv: AndroidTVAsync | FireTVAsync
    dev_opt: dict[str, Any]
AndroidTVConfigEntry = ConfigEntry[AndroidTVRuntimeData]

def get_androidtv_mac(dev_props: dict[str, Any]) -> str | None: ...
def _setup_androidtv(hass: HomeAssistant, config: Mapping[str, Any]) -> tuple[str, PythonRSASigner | None, str]: ...
async def async_connect_androidtv(hass: HomeAssistant, config: Mapping[str, Any], *, state_detection_rules: dict[str, Any] | None = None, timeout: float = 30.0) -> tuple[AndroidTVAsync | FireTVAsync | None, str | None]: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: AndroidTVConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AndroidTVConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: AndroidTVConfigEntry) -> None: ...
