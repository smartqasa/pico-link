from .coordinator import LockData as LockData, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from .entity import SchlageEntity as SchlageEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_SENSOR_DESCRIPTIONS: list[SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SchlageBatterySensor(SchlageEntity, SensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, coordinator: SchlageDataUpdateCoordinator, description: SensorEntityDescription, device_id: str) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
