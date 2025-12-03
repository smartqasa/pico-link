from .config_flow import normalize_hkid as normalize_hkid
from .connection import HKDevice as HKDevice
from .const import DOMAIN as DOMAIN, KNOWN_DEVICES as KNOWN_DEVICES
from .utils import async_get_controller as async_get_controller
from _typeshed import Incomplete
from aiohomekit.controller import ble as ble, coap as coap, ip as ip
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.async_ import create_eager_task as create_eager_task

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
