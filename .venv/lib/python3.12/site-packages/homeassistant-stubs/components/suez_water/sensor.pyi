from .const import CONF_COUNTER_ID as CONF_COUNTER_ID, DOMAIN as DOMAIN
from .coordinator import SuezWaterConfigEntry as SuezWaterConfigEntry, SuezWaterCoordinator as SuezWaterCoordinator, SuezWaterData as SuezWaterData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CURRENCY_EURO as CURRENCY_EURO, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pysuez.const import ATTRIBUTION
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SuezWaterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SuezWaterData], float | str | None]
    attr_fn: Callable[[SuezWaterData], dict[str, Any] | None] = ...

SENSORS: tuple[SuezWaterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SuezWaterConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SuezWaterSensor(CoordinatorEntity[SuezWaterCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    entity_description: SuezWaterSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SuezWaterCoordinator, counter_id: int, entity_description: SuezWaterSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
