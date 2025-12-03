from . import ForecastSolarConfigEntry as ForecastSolarConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import ForecastSolarDataUpdateCoordinator as ForecastSolarDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from forecast_solar.models import Estimate as Estimate
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True)
class ForecastSolarSensorEntityDescription(SensorEntityDescription):
    state: Callable[[Estimate], Any] | None = ...

SENSORS: tuple[ForecastSolarSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ForecastSolarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ForecastSolarSensorEntity(CoordinatorEntity[ForecastSolarDataUpdateCoordinator], SensorEntity):
    entity_description: ForecastSolarSensorEntityDescription
    _attr_has_entity_name: bool
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry_id: str, coordinator: ForecastSolarDataUpdateCoordinator, entity_description: ForecastSolarSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime | StateType: ...
