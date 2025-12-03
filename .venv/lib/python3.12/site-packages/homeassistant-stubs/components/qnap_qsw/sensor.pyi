from .const import ATTR_MAX as ATTR_MAX, DOMAIN as DOMAIN, QSW_COORD_DATA as QSW_COORD_DATA, RPM as RPM
from .coordinator import QswDataCoordinator as QswDataCoordinator
from .entity import QswEntityDescription as QswEntityDescription, QswEntityType as QswEntityType, QswSensorEntity as QswSensorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType, UNDEFINED as UNDEFINED
from typing import Final

@dataclass(frozen=True)
class QswSensorEntityDescription(SensorEntityDescription, QswEntityDescription):
    attributes: dict[str, list[str]] | None = ...
    qsw_type: QswEntityType | None = ...
    sep_key: str = ...
    value_fn: Callable[[str], datetime | StateType] = ...

DEPRECATED_UPTIME_SECONDS: Incomplete
SENSOR_TYPES: Final[tuple[QswSensorEntityDescription, ...]]
LACP_PORT_SENSOR_TYPES: Final[tuple[QswSensorEntityDescription, ...]]
PORT_SENSOR_TYPES: Final[tuple[QswSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class QswSensor(QswSensorEntity, SensorEntity):
    entity_description: QswSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QswDataCoordinator, description: QswSensorEntityDescription, entry: ConfigEntry, type_id: int | None = None) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
