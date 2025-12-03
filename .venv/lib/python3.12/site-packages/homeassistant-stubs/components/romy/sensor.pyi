from .const import DOMAIN as DOMAIN
from .coordinator import RomyVacuumCoordinator as RomyVacuumCoordinator
from .entity import RomyEntity as RomyEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfArea as UnitOfArea, UnitOfLength as UnitOfLength, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS: list[SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RomySensor(RomyEntity, SensorEntity):
    entity_description: SensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RomyVacuumCoordinator, entity_description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int: ...
