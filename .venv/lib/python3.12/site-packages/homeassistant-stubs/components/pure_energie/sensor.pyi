from . import PureEnergieConfigEntry as PureEnergieConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import PureEnergieData as PureEnergieData, PureEnergieDataUpdateCoordinator as PureEnergieDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_HOST as CONF_HOST, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class PureEnergieSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PureEnergieData], int | float]

SENSORS: tuple[PureEnergieSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PureEnergieConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PureEnergieSensorEntity(CoordinatorEntity[PureEnergieDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: PureEnergieSensorEntityDescription
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, description: PureEnergieSensorEntityDescription, entry: PureEnergieConfigEntry) -> None: ...
    @property
    def native_value(self) -> int | float: ...
