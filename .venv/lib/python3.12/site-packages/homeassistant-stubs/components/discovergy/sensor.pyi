from . import DiscovergyConfigEntry as DiscovergyConfigEntry
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import DiscovergyUpdateCoordinator as DiscovergyUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pydiscovergy.models import Reading as Reading

def _get_and_scale(reading: Reading, key: str, scale: int) -> datetime | float | None: ...

@dataclass(frozen=True, kw_only=True)
class DiscovergySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Reading, str, int], datetime | float | None] = field(default=_get_and_scale)
    alternative_keys: list[str] = field(default_factory=list)
    scale: int = field(default_factory=Incomplete)

GAS_SENSORS: tuple[DiscovergySensorEntityDescription, ...]
ELECTRICITY_SENSORS: tuple[DiscovergySensorEntityDescription, ...]
ADDITIONAL_SENSORS: tuple[DiscovergySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: DiscovergyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiscovergySensor(CoordinatorEntity[DiscovergyUpdateCoordinator], SensorEntity):
    entity_description: DiscovergySensorEntityDescription
    data_key: str
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data_key: str, description: DiscovergySensorEntityDescription, coordinator: DiscovergyUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> datetime | float | None: ...
