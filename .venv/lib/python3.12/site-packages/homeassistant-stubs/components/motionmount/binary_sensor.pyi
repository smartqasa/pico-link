import motionmount
from .const import DOMAIN as DOMAIN
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MotionMountMovingSensor(MotionMountEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: ConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...
