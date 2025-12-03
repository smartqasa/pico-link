from .const import DOMAIN as DOMAIN
from .coordinator import GeocachingDataUpdateCoordinator as GeocachingDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from geocachingapi.models import GeocachingStatus as GeocachingStatus
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class GeocachingSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[GeocachingStatus], str | int | None]

SENSORS: tuple[GeocachingSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GeocachingSensor(CoordinatorEntity[GeocachingDataUpdateCoordinator], SensorEntity):
    entity_description: GeocachingSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GeocachingDataUpdateCoordinator, description: GeocachingSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | int | None: ...
