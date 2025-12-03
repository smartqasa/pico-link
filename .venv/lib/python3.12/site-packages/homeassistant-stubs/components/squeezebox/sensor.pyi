from . import SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .const import STATUS_SENSOR_INFO_TOTAL_ALBUMS as STATUS_SENSOR_INFO_TOTAL_ALBUMS, STATUS_SENSOR_INFO_TOTAL_ARTISTS as STATUS_SENSOR_INFO_TOTAL_ARTISTS, STATUS_SENSOR_INFO_TOTAL_DURATION as STATUS_SENSOR_INFO_TOTAL_DURATION, STATUS_SENSOR_INFO_TOTAL_GENRES as STATUS_SENSOR_INFO_TOTAL_GENRES, STATUS_SENSOR_INFO_TOTAL_SONGS as STATUS_SENSOR_INFO_TOTAL_SONGS, STATUS_SENSOR_LASTSCAN as STATUS_SENSOR_LASTSCAN, STATUS_SENSOR_OTHER_PLAYER_COUNT as STATUS_SENSOR_OTHER_PLAYER_COUNT, STATUS_SENSOR_PLAYER_COUNT as STATUS_SENSOR_PLAYER_COUNT
from .entity import LMSStatusEntity as LMSStatusEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

SENSORS: tuple[SensorEntityDescription, ...]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ServerStatusSensor(LMSStatusEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
