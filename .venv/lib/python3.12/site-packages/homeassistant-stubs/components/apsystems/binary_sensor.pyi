from . import ApSystemsConfigEntry as ApSystemsConfigEntry, ApSystemsData as ApSystemsData
from .coordinator import ApSystemsDataCoordinator as ApSystemsDataCoordinator
from .entity import ApSystemsEntity as ApSystemsEntity
from APsystemsEZ1 import ReturnAlarmInfo as ReturnAlarmInfo
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class ApsystemsLocalApiBinarySensorDescription(BinarySensorEntityDescription):
    is_on: Callable[[ReturnAlarmInfo], bool | None]

BINARY_SENSORS: tuple[ApsystemsLocalApiBinarySensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ApSystemsConfigEntry, add_entities: AddEntitiesCallback) -> None: ...

class ApSystemsBinarySensorWithDescription(CoordinatorEntity[ApSystemsDataCoordinator], ApSystemsEntity, BinarySensorEntity):
    entity_description: ApsystemsLocalApiBinarySensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, data: ApSystemsData, entity_description: ApsystemsLocalApiBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
