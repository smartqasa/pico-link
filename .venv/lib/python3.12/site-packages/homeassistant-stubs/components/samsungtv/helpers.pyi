from . import SamsungTVConfigEntry as SamsungTVConfigEntry
from .bridge import SamsungTVBridge as SamsungTVBridge
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

@callback
def async_get_device_entry_by_device_id(hass: HomeAssistant, device_id: str) -> DeviceEntry: ...
@callback
def async_get_device_id_from_entity_id(hass: HomeAssistant, entity_id: str) -> str: ...
@callback
def async_get_client_by_device_entry(hass: HomeAssistant, device: DeviceEntry) -> SamsungTVBridge: ...
