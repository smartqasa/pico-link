from .const import DOMAIN as DOMAIN
from .coordinator import ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tololib import ToloSettings as ToloSettings, ToloStatus as ToloStatus

@dataclass(frozen=True, kw_only=True)
class ToloSensorEntityDescription(SensorEntityDescription):
    getter: Callable[[ToloStatus], int | None]
    availability_checker: Callable[[ToloSettings, ToloStatus], bool] | None
    state_class = ...

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloSensorEntity(ToloSaunaCoordinatorEntity, SensorEntity):
    entity_description: ToloSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry, entity_description: ToloSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> int | None: ...
