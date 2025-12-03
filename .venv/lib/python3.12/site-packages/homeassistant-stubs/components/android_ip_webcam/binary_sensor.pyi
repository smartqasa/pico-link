from .const import MOTION_ACTIVE as MOTION_ACTIVE
from .coordinator import AndroidIPCamConfigEntry as AndroidIPCamConfigEntry, AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from .entity import AndroidIPCamBaseEntity as AndroidIPCamBaseEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BINARY_SENSOR_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AndroidIPCamConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPWebcamBinarySensor(AndroidIPCamBaseEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AndroidIPCamDataUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
