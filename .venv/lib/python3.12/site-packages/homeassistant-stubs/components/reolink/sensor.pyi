from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkHostCoordinatorEntity as ReolinkHostCoordinatorEntity, ReolinkHostEntityDescription as ReolinkHostEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from reolink_aio.api import Host as Host

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkSensorEntityDescription(SensorEntityDescription, ReolinkChannelEntityDescription):
    value: Callable[[Host, int], StateType]

@dataclass(frozen=True, kw_only=True)
class ReolinkHostSensorEntityDescription(SensorEntityDescription, ReolinkHostEntityDescription):
    value: Callable[[Host], StateType]

SENSORS: Incomplete
HOST_SENSORS: Incomplete
HDD_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkSensorEntity(ReolinkChannelCoordinatorEntity, SensorEntity):
    entity_description: ReolinkSensorEntityDescription
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | date | datetime | Decimal: ...

class ReolinkHostSensorEntity(ReolinkHostCoordinatorEntity, SensorEntity):
    entity_description: ReolinkHostSensorEntityDescription
    def __init__(self, reolink_data: ReolinkData, entity_description: ReolinkHostSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | date | datetime | Decimal: ...

class ReolinkHddSensorEntity(ReolinkHostCoordinatorEntity, SensorEntity):
    entity_description: ReolinkSensorEntityDescription
    _hdd_index: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_key: str
    def __init__(self, reolink_data: ReolinkData, hdd_index: int, entity_description: ReolinkSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | date | datetime | Decimal: ...
    @property
    def available(self) -> bool: ...
