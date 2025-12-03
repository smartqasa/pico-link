from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import ReCollectWasteEntity as ReCollectWasteEntity
from .util import async_get_pickup_type_names as async_get_pickup_type_names
from _typeshed import Incomplete
from aiorecollect.client import PickupEvent as PickupEvent
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

ATTR_PICKUP_TYPES: str
ATTR_AREA_NAME: str
SENSOR_TYPE_CURRENT_PICKUP: str
SENSOR_TYPE_NEXT_PICKUP: str
SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReCollectWasteSensor(ReCollectWasteEntity, SensorEntity):
    _attr_device_class: Incomplete
    PICKUP_INDEX_MAP: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[list[PickupEvent]], entry: ConfigEntry, description: SensorEntityDescription) -> None: ...
    _attr_extra_state_attributes: Incomplete
    _attr_native_value: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
