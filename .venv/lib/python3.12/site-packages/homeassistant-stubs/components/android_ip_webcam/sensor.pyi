from .coordinator import AndroidIPCamConfigEntry as AndroidIPCamConfigEntry, AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from .entity import AndroidIPCamBaseEntity as AndroidIPCamBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pydroid_ipcam import PyDroidIPCam as PyDroidIPCam

@dataclass(frozen=True, kw_only=True)
class AndroidIPWebcamSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PyDroidIPCam], StateType]
    unit_fn: Callable[[PyDroidIPCam], str | None] = ...

SENSOR_TYPES: tuple[AndroidIPWebcamSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AndroidIPCamConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPWebcamSensor(AndroidIPCamBaseEntity, SensorEntity):
    entity_description: AndroidIPWebcamSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AndroidIPCamDataUpdateCoordinator, description: AndroidIPWebcamSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
