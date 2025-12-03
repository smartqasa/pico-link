from .coordinator import GoalZeroConfigEntry as GoalZeroConfigEntry
from .entity import GoalZeroEntity as GoalZeroEntity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int
BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GoalZeroConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GoalZeroBinarySensor(GoalZeroEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
