from .const import GATEWAY_SERIAL_PATTERN as GATEWAY_SERIAL_PATTERN, PLATFORMS as PLATFORMS
from devolo_home_control_api.homecontrol import HomeControl
from devolo_home_control_api.mydevolo import Mydevolo
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from types import MappingProxyType
from typing import Any

type DevoloHomeControlConfigEntry = ConfigEntry[list[HomeControl]]
async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...
def configure_mydevolo(conf: dict[str, Any] | MappingProxyType[str, Any]) -> Mydevolo: ...
