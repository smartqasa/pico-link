from .const import DOMAIN as DOMAIN
from .coordinator import StookwijzerConfigEntry as StookwijzerConfigEntry, StookwijzerCoordinator as StookwijzerCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfSpeed as UnitOfSpeed
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from stookwijzer import Stookwijzer as Stookwijzer

@dataclass(kw_only=True, frozen=True)
class StookwijzerSensorDescription(SensorEntityDescription):
    value_fn: Callable[[Stookwijzer], int | float | str | None]

STOOKWIJZER_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: StookwijzerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StookwijzerSensor(CoordinatorEntity[StookwijzerCoordinator], SensorEntity):
    entity_description: StookwijzerSensorDescription
    _attr_attribution: str
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, description: StookwijzerSensorDescription, entry: StookwijzerConfigEntry) -> None: ...
    @property
    def native_value(self) -> int | float | str | None: ...
