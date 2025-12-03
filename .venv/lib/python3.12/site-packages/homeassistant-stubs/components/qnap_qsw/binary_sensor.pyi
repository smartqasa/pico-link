from .const import ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN, QSW_COORD_DATA as QSW_COORD_DATA
from .coordinator import QswDataCoordinator as QswDataCoordinator
from .entity import QswEntityDescription as QswEntityDescription, QswEntityType as QswEntityType, QswSensorEntity as QswSensorEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from typing import Final

@dataclass(frozen=True)
class QswBinarySensorEntityDescription(BinarySensorEntityDescription, QswEntityDescription):
    attributes: dict[str, list[str]] | None = ...
    qsw_type: QswEntityType | None = ...
    sep_key: str = ...

BINARY_SENSOR_TYPES: Final[tuple[QswBinarySensorEntityDescription, ...]]
LACP_PORT_BINARY_SENSOR_TYPES: Final[tuple[QswBinarySensorEntityDescription, ...]]
PORT_BINARY_SENSOR_TYPES: Final[tuple[QswBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class QswBinarySensor(QswSensorEntity, BinarySensorEntity):
    entity_description: QswBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QswDataCoordinator, description: QswBinarySensorEntityDescription, entry: ConfigEntry, type_id: int | None = None) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
