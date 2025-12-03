from .const import DOMAIN as DOMAIN
from .coordinator import SonarrDataT as SonarrDataT, SonarrDataUpdateCoordinator as SonarrDataUpdateCoordinator
from .entity import SonarrEntity as SonarrEntity
from aiopyarr import Diskspace, SonarrQueue, SonarrWantedMissing
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, Generic

@dataclass(frozen=True)
class SonarrSensorEntityDescriptionMixIn(Generic[SonarrDataT]):
    attributes_fn: Callable[[SonarrDataT], dict[str, str]]
    value_fn: Callable[[SonarrDataT], StateType]

@dataclass(frozen=True)
class SonarrSensorEntityDescription(SensorEntityDescription, SonarrSensorEntityDescriptionMixIn[SonarrDataT]): ...

def get_disk_space_attr(disks: list[Diskspace]) -> dict[str, str]: ...
def get_queue_attr(queue: SonarrQueue) -> dict[str, str]: ...
def get_wanted_attr(wanted: SonarrWantedMissing) -> dict[str, str]: ...

SENSOR_TYPES: dict[str, SonarrSensorEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SonarrSensor(SonarrEntity[SonarrDataT], SensorEntity):
    coordinator: SonarrDataUpdateCoordinator[SonarrDataT]
    entity_description: SonarrSensorEntityDescription[SonarrDataT]
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    @property
    def native_value(self) -> StateType: ...
