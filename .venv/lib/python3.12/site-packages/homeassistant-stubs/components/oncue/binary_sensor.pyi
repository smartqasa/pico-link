from .entity import OncueEntity as OncueEntity
from .types import OncueConfigEntry as OncueConfigEntry
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]
SENSOR_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OncueConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OncueBinarySensorEntity(OncueEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
