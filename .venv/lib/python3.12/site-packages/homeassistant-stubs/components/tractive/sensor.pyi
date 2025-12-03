from . import Trackables as Trackables, TractiveClient as TractiveClient, TractiveConfigEntry as TractiveConfigEntry
from .const import ATTR_ACTIVITY_LABEL as ATTR_ACTIVITY_LABEL, ATTR_CALORIES as ATTR_CALORIES, ATTR_DAILY_GOAL as ATTR_DAILY_GOAL, ATTR_MINUTES_ACTIVE as ATTR_MINUTES_ACTIVE, ATTR_MINUTES_DAY_SLEEP as ATTR_MINUTES_DAY_SLEEP, ATTR_MINUTES_NIGHT_SLEEP as ATTR_MINUTES_NIGHT_SLEEP, ATTR_MINUTES_REST as ATTR_MINUTES_REST, ATTR_SLEEP_LABEL as ATTR_SLEEP_LABEL, ATTR_TRACKER_STATE as ATTR_TRACKER_STATE, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED, TRACKER_WELLNESS_STATUS_UPDATED as TRACKER_WELLNESS_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class TractiveSensorEntityDescription(SensorEntityDescription):
    signal_prefix: str
    hardware_sensor: bool = ...
    value_fn: Callable[[StateType], StateType] = ...

class TractiveSensor(TractiveEntity, SensorEntity):
    entity_description: TractiveSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_available: bool
    def __init__(self, client: TractiveClient, item: Trackables, description: TractiveSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def handle_status_update(self, event: dict[str, Any]) -> None: ...

SENSOR_TYPES: tuple[TractiveSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TractiveConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
