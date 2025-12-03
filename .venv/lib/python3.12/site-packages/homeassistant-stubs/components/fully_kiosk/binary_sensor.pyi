from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullyBinarySensor(FullyKioskEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
