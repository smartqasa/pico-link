from . import PECOCoordinatorData as PECOCoordinatorData
from .const import ATTR_CONTENT as ATTR_CONTENT, CONF_COUNTY as CONF_COUNTY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Final

@dataclass(frozen=True, kw_only=True)
class PECOSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PECOCoordinatorData], int | str]
    attribute_fn: Callable[[PECOCoordinatorData], dict[str, str]]

PARALLEL_UPDATES: Final[int]
SENSOR_LIST: tuple[PECOSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PecoSensor(CoordinatorEntity[DataUpdateCoordinator[PECOCoordinatorData]], SensorEntity):
    entity_description: PECOSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, description: PECOSensorEntityDescription, county: str, coordinator: DataUpdateCoordinator[PECOCoordinatorData]) -> None: ...
    @property
    def native_value(self) -> int | str: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
