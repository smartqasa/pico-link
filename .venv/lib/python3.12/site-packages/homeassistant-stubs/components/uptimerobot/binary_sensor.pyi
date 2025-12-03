from .const import DOMAIN as DOMAIN
from .coordinator import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from .entity import UptimeRobotEntity as UptimeRobotEntity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UptimeRobotBinarySensor(UptimeRobotEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
