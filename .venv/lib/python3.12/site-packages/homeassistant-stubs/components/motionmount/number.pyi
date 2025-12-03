import motionmount
from .const import DOMAIN as DOMAIN
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MotionMountExtension(MotionMountEntity, NumberEntity):
    _attr_native_max_value: int
    _attr_native_min_value: int
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...

class MotionMountTurn(MotionMountEntity, NumberEntity):
    _attr_native_max_value: int
    _attr_native_min_value: int
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
