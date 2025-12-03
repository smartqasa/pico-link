from .coordinator import RAVEnConfigEntry as RAVEnConfigEntry, RAVEnDataCoordinator as RAVEnDataCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_MAC as CONF_MAC, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True, kw_only=True)
class RAVEnSensorEntityDescription(SensorEntityDescription):
    message_key: str
    attribute_keys: list[str] | None = ...

SENSORS: Incomplete
DIAGNOSTICS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RAVEnConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RAVEnSensor(CoordinatorEntity[RAVEnDataCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: RAVEnSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RAVEnDataCoordinator, entity_description: RAVEnSensorEntityDescription) -> None: ...
    @property
    def _data(self) -> Any: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def native_value(self) -> StateType: ...

class RAVEnMeterSensor(RAVEnSensor):
    _meter_mac_addr: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RAVEnDataCoordinator, entity_description: RAVEnSensorEntityDescription, meter_mac_addr: str) -> None: ...
    @property
    def _data(self) -> Any: ...
