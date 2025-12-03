from . import Eq3ConfigEntry as Eq3ConfigEntry
from .const import ENTITY_KEY_BATTERY as ENTITY_KEY_BATTERY, ENTITY_KEY_DST as ENTITY_KEY_DST, ENTITY_KEY_WINDOW as ENTITY_KEY_WINDOW
from .entity import Eq3Entity as Eq3Entity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from eq3btsmart.models import Status as Status
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class Eq3BinarySensorEntityDescription(BinarySensorEntityDescription):
    value_func: Callable[[Status], bool]

BINARY_SENSOR_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Eq3ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Eq3BinarySensorEntity(Eq3Entity, BinarySensorEntity):
    entity_description: Eq3BinarySensorEntityDescription
    def __init__(self, entry: Eq3ConfigEntry, entity_description: Eq3BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
