from . import Eq3ConfigEntry as Eq3ConfigEntry
from .const import ENTITY_KEY_AWAY_UNTIL as ENTITY_KEY_AWAY_UNTIL, ENTITY_KEY_VALVE as ENTITY_KEY_VALVE
from .entity import Eq3Entity as Eq3Entity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from eq3btsmart.models import Status as Status
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.components.sensor.const import SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class Eq3SensorEntityDescription(SensorEntityDescription):
    value_func: Callable[[Status], int | datetime | None]

SENSOR_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Eq3ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Eq3SensorEntity(Eq3Entity, SensorEntity):
    entity_description: Eq3SensorEntityDescription
    def __init__(self, entry: Eq3ConfigEntry, entity_description: Eq3SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | datetime | None: ...
