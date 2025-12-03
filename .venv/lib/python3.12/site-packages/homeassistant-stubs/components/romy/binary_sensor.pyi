from .const import DOMAIN as DOMAIN
from .coordinator import RomyVacuumCoordinator as RomyVacuumCoordinator
from .entity import RomyEntity as RomyEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BINARY_SENSORS: list[BinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RomyBinarySensor(RomyEntity, BinarySensorEntity):
    entity_description: BinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RomyVacuumCoordinator, entity_description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
