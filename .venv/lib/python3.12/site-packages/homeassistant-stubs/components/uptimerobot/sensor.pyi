from .const import DOMAIN as DOMAIN
from .coordinator import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from .entity import UptimeRobotEntity as UptimeRobotEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS_INFO: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UptimeRobotSensor(UptimeRobotEntity, SensorEntity):
    @property
    def native_value(self) -> str: ...
