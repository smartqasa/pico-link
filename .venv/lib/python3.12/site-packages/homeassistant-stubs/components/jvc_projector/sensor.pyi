from . import JVCConfigEntry as JVCConfigEntry, JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from .entity import JvcProjectorEntity as JvcProjectorEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

JVC_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JvcSensor(JvcProjectorEntity, SensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | None: ...
