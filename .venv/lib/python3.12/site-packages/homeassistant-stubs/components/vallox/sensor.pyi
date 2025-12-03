from .const import DOMAIN as DOMAIN, METRIC_KEY_MODE as METRIC_KEY_MODE, MODE_ON as MODE_ON, VALLOX_CELL_STATE_TO_STR as VALLOX_CELL_STATE_TO_STR, VALLOX_PROFILE_TO_PRESET_MODE as VALLOX_PROFILE_TO_PRESET_MODE
from .coordinator import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

class ValloxSensorEntity(ValloxEntity, SensorEntity):
    entity_description: ValloxSensorEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...

class ValloxProfileSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> StateType: ...

class ValloxFanSpeedSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> StateType | datetime: ...

class ValloxFilterRemainingSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> StateType | datetime: ...

class ValloxCellStateSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> StateType: ...

class ValloxProfileDurationSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> StateType: ...

@dataclass(frozen=True)
class ValloxSensorEntityDescription(SensorEntityDescription):
    metric_key: str | None = ...
    entity_type: type[ValloxSensorEntity] = ...
    round_ndigits: int | None = ...

SENSOR_ENTITIES: tuple[ValloxSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
