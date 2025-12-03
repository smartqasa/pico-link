from . import TautulliConfigEntry as TautulliConfigEntry
from .const import ATTR_TOP_USER as ATTR_TOP_USER, DOMAIN as DOMAIN
from .coordinator import TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from .entity import TautulliEntity as TautulliEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from pytautulli import PyTautulliApiActivity as PyTautulliApiActivity, PyTautulliApiHomeStats as PyTautulliApiHomeStats, PyTautulliApiSession as PyTautulliApiSession, PyTautulliApiUser as PyTautulliApiUser

def get_top_stats(home_stats: PyTautulliApiHomeStats, activity: PyTautulliApiActivity, key: str) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class TautulliSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PyTautulliApiHomeStats, PyTautulliApiActivity, str], StateType]

SENSOR_TYPES: tuple[TautulliSensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class TautulliSessionSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PyTautulliApiSession], StateType]

SESSION_SENSOR_TYPES: tuple[TautulliSessionSensorEntityDescription, ...]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: TautulliConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TautulliSensor(TautulliEntity, SensorEntity):
    entity_description: TautulliSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

class TautulliSessionSensor(TautulliEntity, SensorEntity):
    entity_description: TautulliSessionSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TautulliDataUpdateCoordinator, description: EntityDescription, user: PyTautulliApiUser) -> None: ...
    @property
    def native_value(self) -> StateType: ...
