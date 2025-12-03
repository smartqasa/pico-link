from . import TVFerryConfigEntry as TVFerryConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import as_utc as as_utc
from typing import Any

ATTR_FROM: str
ATTR_TO: str
ATTR_MODIFIED_TIME: str
ATTR_OTHER_INFO: str
SCAN_INTERVAL: Incomplete

@dataclass(frozen=True, kw_only=True)
class TrafikverketSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType | datetime]
    info_fn: Callable[[dict[str, Any]], StateType | list] | None

SENSOR_TYPES: tuple[TrafikverketSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TVFerryConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FerrySensor(CoordinatorEntity[TVDataUpdateCoordinator], SensorEntity):
    entity_description: TrafikverketSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, name: str, entry_id: str, entity_description: TrafikverketSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _update_attr(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
