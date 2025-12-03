from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

STATE_FIRST_QUARTER: str
STATE_FULL_MOON: str
STATE_LAST_QUARTER: str
STATE_NEW_MOON: str
STATE_WANING_CRESCENT: str
STATE_WANING_GIBBOUS: str
STATE_WAXING_CRESCENT: str
STATE_WAXING_GIBBOUS: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MoonSensorEntity(SensorEntity):
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
