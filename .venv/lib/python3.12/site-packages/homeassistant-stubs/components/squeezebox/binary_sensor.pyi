from . import SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .const import STATUS_SENSOR_NEEDSRESTART as STATUS_SENSOR_NEEDSRESTART, STATUS_SENSOR_RESCAN as STATUS_SENSOR_RESCAN
from .entity import LMSStatusEntity as LMSStatusEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS: tuple[BinarySensorEntityDescription, ...]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ServerStatusBinarySensor(LMSStatusEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
