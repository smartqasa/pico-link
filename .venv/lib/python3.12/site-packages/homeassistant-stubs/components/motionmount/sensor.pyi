import motionmount
from .const import DOMAIN as DOMAIN
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MotionMountErrorStatusSensor(MotionMountEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> str: ...
