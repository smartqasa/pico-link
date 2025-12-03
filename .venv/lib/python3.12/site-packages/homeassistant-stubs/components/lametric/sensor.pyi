from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from demetriek import Device as Device
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class LaMetricSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Device], int | None]

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMetricSensorEntity(LaMetricEntity, SensorEntity):
    entity_description: LaMetricSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
