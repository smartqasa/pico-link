from .const import DOMAIN as DOMAIN
from .entity import LookinDeviceCoordinatorEntity as LookinDeviceCoordinatorEntity
from .models import LookinData as LookinData
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

LOGGER: Incomplete
SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LookinSensorEntity(LookinDeviceCoordinatorEntity, SensorEntity):
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, description: SensorEntityDescription, lookin_data: LookinData) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
