from . import device_trigger as device_trigger
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .entity import async_setup_non_entity_entry_helper as async_setup_non_entity_entry_helper
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

AUTOMATION_TYPE_TRIGGER: str
AUTOMATION_TYPES: Incomplete
AUTOMATION_TYPES_SCHEMA: Incomplete
CONF_AUTOMATION_TYPE: str
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def _async_setup_automation(hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType) -> None: ...
async def async_removed_from_device(hass: HomeAssistant, device_id: str) -> None: ...
