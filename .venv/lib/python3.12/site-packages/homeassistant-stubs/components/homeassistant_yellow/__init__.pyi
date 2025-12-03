from .const import FIRMWARE as FIRMWARE, RADIO_DEVICE as RADIO_DEVICE, ZHA_HW_DISCOVERY_DATA as ZHA_HW_DISCOVERY_DATA
from _typeshed import Incomplete
from homeassistant.components.hassio import get_os_info as get_os_info
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import check_multi_pan_addon as check_multi_pan_addon
from homeassistant.components.homeassistant_hardware.util import ApplicationType as ApplicationType, guess_firmware_type as guess_firmware_type
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HARDWARE as SOURCE_HARDWARE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.hassio import is_hassio as is_hassio

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
